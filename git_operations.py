import os
import git
print(git.__file__)
# Set your project path
PROJECT_PATH = r"C:\python projects\projectplanvisualization"

GITHUB_REPO_URL = "https://github.com/Jyosh8/dynamic-visualization"

def push_to_github():
    repo_path = PROJECT_PATH

    # Initialize Git repository if not exists
    if not os.path.exists(os.path.join(repo_path, ".git")):
        repo = git.Repo.init(repo_path)
        print("✅ Initialized Git repository.")
    else:
        repo = git.Repo(repo_path)
        print("🔄 Using existing Git repository.")

    origin_exists = any(remote.name == "origin" for remote in repo.remotes)

    if not origin_exists:
        repo.create_remote("origin", GITHUB_REPO_URL)
        print(f"🌍 Added remote repository: {GITHUB_REPO_URL}")

    repo.git.add(all=True)
    repo.index.commit("Updated Streamlit project")
    repo.git.push("--set-upstream", "origin", "main")
    print("🚀 Successfully pushed to GitHub!")

if __name__ == "__main__":
    push_to_github()
