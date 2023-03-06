import re

from gitlint import git, rules


class BranchName(rules.CommitRule):
    """Rule to validate branch name."""
    name = "branch-name"
    id = ""

    def validate(
        self,
        commit: git.StagedLocalGitCommit,
    ) -> list[rules.RuleViolation] | None:
        """Validate branch name."""
        branch_name_format = r"^(feature)\/(?:[a-z0-9-]*)+$"
        current_branch = commit.context.current_branch
        # Ignore rule during rebase
        if current_branch == "HEAD":
            return None
        if re.fullmatch(branch_name_format, current_branch):
            return None

        msg = (
            "Branch name is not valid. "
            "Template: feature/[short-and-meaningful-description]. "
            f"Got: {current_branch}."
        )
        return [rules.RuleViolation(self.id, msg, line_nr=1)]
