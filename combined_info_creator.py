from github import Github, GithubException
import os


def main():
    token = os.getenv('GITHUB_TOKEN')
    org_name = 'dataloop-ai-joint-dev'

    g = Github(token)
    org = g.get_organization(org_name)
    repo_links = ""

    combined_readme_content = ""
    go_to_top = "\n \n[Go To Top](#solution-engineering-catalog)"
    repos = sorted(org.get_repos(), key=lambda x: x.name)
    for repo in repos:
        try:
            if repo.name.endswith("-dataloop".lower()):
                continue
            repo_info = f"\n# {repo.name}\nVisibility: {repo.private and 'Private' or 'Public'}\n"
            readme_content = repo.get_contents("INFO.md").decoded_content.decode('utf-8')
            print(f"Name: {repo.name}, Visibility {repo.visibility}")
            combined_readme_content += repo_info + readme_content + go_to_top + "\n---\n"
            repo_links += f"* [{repo.name}](#{repo.name})\n\n"
        except GithubException as e:
            if e.status != 404:
                print(f"Error: {e}")

    html_header = """
<p align="center">
<a href="https://dataloop.ai/" target="_blank" rel="noreferrer noopener">
<img width="700" src="https://github.com/dataloop-ai-joint-dev/.github/blob/master/logo.png"></a>
</p>

<div align="center">
<a href="https://www.linkedin.com/company/dataloop/about/" target="_blank" rel="noreferrer noopener">
<img src="https://github.com/dataloop-ai-joint-dev/.github/blob/master/LinkedIn.png" width="3%" alt="LinkedIn"></a>
<a href="https://www.youtube.com/channel/UCCvp-nw5mK9bb9lDNcD6fgw/featured" target="_blank" rel="noreferrer noopener">
<img src="https://github.com/dataloop-ai-joint-dev/.github/blob/master/YouTube.jpeg" width="3%" alt="YouTube"></a>
<a href="https://github.com/dataloop-ai-joint-dev" target="_blank" rel="noreferrer noopener">
<img src="https://github.com/dataloop-ai-joint-dev/.github/blob/master/GitHub.png" width="3%" alt="GitHub"></a>
</div>
"""
    header = "# Solution Engineering Catalog\n\n" + html_header + "\n---\n" + "## Available Solutions:\n\n"

    combined_readme_content = header + repo_links + "\n---\n" + combined_readme_content
    with open("Combined_README.md", "w") as file:
        file.write(combined_readme_content)

    # Update new readme file to .github repo
    github_repo = g.get_repo(f"{org_name}/.github")

    try:
        # If the README.md doesn't exist, create it
        github_repo.create_file("profile/README.md", "commit message", combined_readme_content)
    except:
        # If the README.md exists, update it
        readme_file = github_repo.get_contents("profile/README.md")
        github_repo.update_file(readme_file.path, "commit message", combined_readme_content, readme_file.sha)

    print("Combined README file created")


if __name__ == "__main__":
    main()
