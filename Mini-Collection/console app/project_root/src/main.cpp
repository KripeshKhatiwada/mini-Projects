#include "filemanager.h"
#include <iostream>

void showMenu() {
    std::cout << "\n=== File Manager Menu ===\n";
    std::cout << "1. Show Current Directory\n";
    std::cout << "2. Navigate to a Directory\n";
    std::cout << "3. Navigate Back\n";
    std::cout << "4. Navigate Home\n";
    std::cout << "5. Create a File\n";
    std::cout << "6. Delete a File\n";
    std::cout << "0. Exit\n";
    std::cout << "Enter your choice: ";
}

int main() {
    int choice;
    std::string input;

    while (true) {
        showMenu();
        std::cin >> choice;

        switch (choice) {
            case 1:
                showCurrentDirectory();
            break;
            case 2:
                std::cout << "Enter directory path: ";
            std::getline(std::cin, input);
            navigateToDirectory(input);
            break;
            case 3:
                navigateBack();
            break;
            case 4:
                navigateHome();
            break;
            case 5:
                std::cout << "Enter filename: ";
            std::getline(std::cin, input);
            createFile(input);
            break;
            case 6:
                std::cout << "Enter filename to delete: ";
            std::getline(std::cin, input);
            deleteFile(input);
            break;
            case 0:
                std::cout << "Exiting program...\n";
            return 0;
            default:
                std::cout << "Invalid choice, please try again.\n";
        }
    }
}
