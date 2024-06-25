#include <iostream>
#include <cstdlib> // for system()

using namespace std;

int main(int argc, char *argv[]) {
    if (argc < 2) {
        cout << "Usage: " << argv[0] << " \"commit message\"" << endl;
        return 1;
    }

    string commitMessage = argv[1];

    // Combine all arguments into a single commit message
    for (int i = 2; i < argc; ++i) {
        commitMessage += " ";
        commitMessage += argv[i];
    }

    // Git commands
    string gitAdd = "git add .";
    string gitCommit = "git commit -m \"" + commitMessage + "\"";
    string gitPush = "git push --force origin main";

    // Execute Git commands
    system(gitAdd.c_str());
    system(gitCommit.c_str());
    system(gitPush.c_str());

    return 0;
}
