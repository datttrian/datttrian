import requests

ENVS = {
    "staging": "backend-staging.usummitapp.com",
    "dev": "backend-dev.usummitapp.com",
}

CHECKS = ["Cache", "Database", "Email"]
REQUEST_TIMEOUT_SEC = 20


def main(env: str) -> str:
    """Run development sites health-checks.

    This function goes to a corresponding env site, gets current health checks
    state.

    Raises:
        ValueError: the given environment is not available.
        HTTPError: response came with an error.
        ValueError: environment contains some errors.

    """
    print(f"Env: {env}")

    if env not in ENVS:
        raise ValueError(f"{env} environment is not available")

    checks_params = "&".join([f"checks={check}" for check in CHECKS])
    domain = ENVS[env]

    health_check_url = (
        f"https://{domain}/api/v1/utils/health-check/"
        f"?{checks_params}"
    )

    http_response = requests.get(health_check_url, timeout=REQUEST_TIMEOUT_SEC)

    status_code = http_response.status_code
    data = http_response.json()

    health_check_message_pattern = "Health check: {message}"

    print(
        health_check_message_pattern.format(
            message=f"status {status_code}, content: {data}",
        ),
    )

    if status_code != 200:
        print(f"Env: {env} error (unknown) [{status_code}] status")
        raise requests.exceptions.HTTPError(
            health_check_message_pattern.format(
                message="unknown error",
            ),
        )

    errors = [check for check, status in data.items() if status != "OK"]
    if errors:
        print(f"Env: {env} error - {', '.join(errors)}")
        raise ValueError(
            health_check_message_pattern.format(
                message=f"{', '.join(errors)} errors",
            ),
        )

    print(f"Env: {env} success - {data}")
    return health_check_message_pattern.format(message="ok")


if __name__ == "__main__":
    main("dev")
