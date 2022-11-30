## Project File System - Need to knows
Users are restricted from uploading data in the home directory. Any data stored here does not persist restarts, and users run the risk of data loss if the tool is terminated. Users shhould should rather stored data in either one of the two locations: private_branch or project_data.

### private_branch
- Coeus automatically creates a Git Project and maps this private_branch directory whose contents are manged via git.
- Coeus creates a feature branch within the Git Project for added project members. The feature branch is named after the member's email address.
- Users can use the built in JupyterLab terminal to execute git and other file system commands.

### project_data
- The project_data directory, aka shared_folder, is not managed by Git and is designed as a storage space where team members can collaborate using project specific data.
- Data within this directory is only accessable from within the project and by team members.
