import os
import subprocess

def push_to_github(repo_url, local_clone_dir, drive_streamlit_path, commit_message="Auto-push from Colab"):
    # Set up Git identity
    subprocess.run(["git", "config", "--global", "user.email", "you@example.com"], check=True)
    subprocess.run(["git", "config", "--global", "user.name", "Your Name"], check=True)

    # Clone repo
    if not os.path.exists(local_clone_dir):
        subprocess.run(["git", "clone", repo_url, local_clone_dir], check=True)

    # Copy Streamlit-ready assistants into the repo
    os.system(f"cp -r {drive_streamlit_path}/* {local_clone_dir}/")

    # Commit and push
    os.chdir(local_clone_dir)
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", commit_message], check=True)
    subprocess.run(["git", "push"], check=True)

    print("✅ Successfully pushed to GitHub.")

# Example usage:
# push_to_github(
#     repo_url="https://github.com/your-username/your-repo.git",
#     local_clone_dir="/content/your-repo",
#     drive_streamlit_path="/content/drive/MyDrive/assistant_markdown/streamlit_ready/",
#     commit_message="v1.0 assistants"
# )
