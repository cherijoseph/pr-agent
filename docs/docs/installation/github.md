## Run as a GitHub Action

You can use our pre-built Github Action Docker image to run PR-Agent as a Github Action.

1) Add the following file to your repository under `.github/workflows/pr_agent.yml`:

```yaml
on:
  pull_request:
    types: [opened, reopened, ready_for_review]
  issue_comment:
jobs:
  pr_agent_job:
    if: ${{ github.event.sender.type != 'Bot' }}
    runs-on: ubuntu-latest
    permissions:
      issues: write
      pull-requests: write
      contents: write
    name: Run pr agent on every pull request, respond to user comments
    steps:
      - name: PR Agent action step
        id: pragent
        uses: qodo-ai/pr-agent@main
        env:
          OPENAI_KEY: ${{ secrets.OPENAI_KEY }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

2) Add the following secret to your repository under `Settings > Secrets and variables > Actions > New repository secret > Add secret`:

```
Name = OPENAI_KEY
Secret = <your key>
```

The GITHUB_TOKEN secret is automatically created by GitHub.

3) Merge this change to your main branch.
When you open your next PR, you should see a comment from `github-actions` bot with a review of your PR, and instructions on how to use the rest of the tools.

4) You may configure Qodo Merge by adding environment variables under the env section corresponding to any configurable property in the [configuration](https://github.com/Codium-ai/pr-agent/blob/main/pr_agent/settings/configuration.toml) file. Some examples:

```yaml
      env:
        # ... previous environment values
        OPENAI.ORG: "<Your organization name under your OpenAI account>"
        PR_REVIEWER.REQUIRE_TESTS_REVIEW: "false" # Disable tests review
        PR_CODE_SUGGESTIONS.NUM_CODE_SUGGESTIONS: 6 # Increase number of code suggestions
```

See detailed usage instructions in the [USAGE GUIDE](https://qodo-merge-docs.qodo.ai/usage-guide/automations_and_usage/#github-action)

### Using a specific release

!!! tip ""
    if you want to pin your action to a specific release (v0.23 for example) for stability reasons, use:
    ```yaml
    ...
        steps:
          - name: PR Agent action step
            id: pragent
            uses: docker://codiumai/pr-agent:0.23-github_action
    ...
    ```

    For enhanced security, you can also specify the Docker image by its [digest](https://hub.docker.com/repository/docker/codiumai/pr-agent/tags):
    ```yaml
    ...
        steps:
          - name: PR Agent action step
            id: pragent
            uses: docker://codiumai/pr-agent@sha256:14165e525678ace7d9b51cda8652c2d74abb4e1d76b57c4a6ccaeba84663cc64
    ...
    ```

### Action for GitHub enterprise server

!!! tip ""
    To use the action with a GitHub enterprise server, add an environment variable `GITHUB.BASE_URL` with the API URL of your GitHub server.

    For example, if your GitHub server is at `https://github.mycompany.com`, add the following to your workflow file:
    ```yaml
          env:
            # ... previous environment values
            GITHUB.BASE_URL: "https://github.mycompany.com/api/v3"
    ```

---

## Run as a GitHub App

Allowing you to automate the review process on your private or public repositories.

1) Create a GitHub App from the [Github Developer Portal](https://docs.github.com/en/developers/apps/creating-a-github-app).

   - Set the following permissions:
     - Pull requests: Read & write
     - Issue comment: Read & write
     - Metadata: Read-only
     - Contents: Read-only
   - Set the following events:
     - Issue comment
     - Pull request
     - Push (if you need to enable triggering on PR update)

2) Generate a random secret for your app, and save it for later. For example, you can use:

```bash
WEBHOOK_SECRET=$(python -c "import secrets; print(secrets.token_hex(10))")
```

3) Acquire the following pieces of information from your app's settings page:

   - App private key (click "Generate a private key" and save the file)
   - App ID

4) Clone this repository:

```bash
git clone https://github.com/Codium-ai/pr-agent.git
```

5) Copy the secrets template file and fill in the following:

```bash
cp pr_agent/settings/.secrets_template.toml pr_agent/settings/.secrets.toml
# Edit .secrets.toml file
```

- Your OpenAI key.
- Copy your app's private key to the private_key field.
- Copy your app's ID to the app_id field.
- Copy your app's webhook secret to the webhook_secret field.
- Set deployment_type to 'app' in [configuration.toml](https://github.com/Codium-ai/pr-agent/blob/main/pr_agent/settings/configuration.toml)

    > The .secrets.toml file is not copied to the Docker image by default, and is only used for local development.
    > If you want to use the .secrets.toml file in your Docker image, you can add remove it from the .dockerignore file.
    > In most production environments, you would inject the secrets file as environment variables or as mounted volumes.
    > For example, in order to inject a secrets file as a volume in a Kubernetes environment you can update your pod spec to include the following,
    > assuming you have a secret named `pr-agent-settings` with a key named `.secrets.toml`:

    ```
           volumes:
            - name: settings-volume
              secret:
                secretName: pr-agent-settings
    // ...
           containers:
    // ...
              volumeMounts:
                - mountPath: /app/pr_agent/settings_prod
                  name: settings-volume
    ```

    > Another option is to set the secrets as environment variables in your deployment environment, for example `OPENAI.KEY` and `GITHUB.USER_TOKEN`.

6) Build a Docker image for the app and optionally push it to a Docker repository. We'll use Dockerhub as an example:

    ```bash
    docker build . -t codiumai/pr-agent:github_app --target github_app -f docker/Dockerfile
    docker push codiumai/pr-agent:github_app  # Push to your Docker repository
    ```

7. Host the app using a server, serverless function, or container environment. Alternatively, for development and
   debugging, you may use tools like smee.io to forward webhooks to your local machine.
    You can check [Deploy as a Lambda Function](#deploy-as-a-lambda-function)

8. Go back to your app's settings, and set the following:

   - Webhook URL: The URL of your app's server or the URL of the smee.io channel.
   - Webhook secret: The secret you generated earlier.

9. Install the app by navigating to the "Install App" tab and selecting your desired repositories.

> **Note:** When running Qodo Merge from GitHub app, the default configuration file (configuration.toml) will be loaded.
> However, you can override the default tool parameters by uploading a local configuration file `.pr_agent.toml`
> For more information please check out the [USAGE GUIDE](../usage-guide/automations_and_usage.md#github-app)
---

## Deploy as a Lambda Function

Note that since AWS Lambda env vars cannot have "." in the name, you can replace each "." in an env variable with "__".<br>
For example: `GITHUB.WEBHOOK_SECRET` --> `GITHUB__WEBHOOK_SECRET`

1. Follow steps 1-5 from [here](#run-as-a-github-app).
2. Build a docker image that can be used as a lambda function

    ```shell
    docker buildx build --platform=linux/amd64 . -t codiumai/pr-agent:serverless -f docker/Dockerfile.lambda
   ```

3. Push image to ECR

    ```shell
    docker tag codiumai/pr-agent:serverless <AWS_ACCOUNT>.dkr.ecr.<AWS_REGION>.amazonaws.com/codiumai/pr-agent:serverless
    docker push <AWS_ACCOUNT>.dkr.ecr.<AWS_REGION>.amazonaws.com/codiumai/pr-agent:serverless
    ```

4. Create a lambda function that uses the uploaded image. Set the lambda timeout to be at least 3m.
5. Configure the lambda function to have a Function URL.
6. In the environment variables of the Lambda function, specify `AZURE_DEVOPS_CACHE_DIR` to a writable location such as /tmp. (see [link](https://github.com/Codium-ai/pr-agent/pull/450#issuecomment-1840242269))
7. Go back to steps 8-9 of [Method 5](#run-as-a-github-app) with the function url as your Webhook URL.
    The Webhook URL would look like `https://<LAMBDA_FUNCTION_URL>/api/v1/github_webhooks`

### Using AWS Secrets Manager

For production Lambda deployments, use AWS Secrets Manager instead of environment variables:

1. Create a secret in AWS Secrets Manager with JSON format like this:

```json
{
  "openai.key": "sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "github.webhook_secret": "your-webhook-secret-from-step-2",
  "github.private_key": "-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEA...\n-----END RSA PRIVATE KEY-----"
}
```

2. Add IAM permission `secretsmanager:GetSecretValue` to your Lambda execution role
3. Set these environment variables in your Lambda:

```bash
AWS_SECRETS_MANAGER__SECRET_ARN=arn:aws:secretsmanager:us-east-1:123456789012:secret:pr-agent-secrets-AbCdEf
CONFIG__SECRET_PROVIDER=aws_secrets_manager
```

