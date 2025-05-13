#include "filemanager.h"
#include <iostream>
#include <filesystem>  // For handling directories
#include <fstream>     // For file operations

namespace fs = std::filesystem;

void showCurrentDirectory() {
    std::cout << "Current Directory: " << fs::current_path() << std::endl;
}

void navigateToDirectory(const std::string& path) {
    if (fs::exists(path) && fs::is_directory(path)) {
        fs::current_path(path);
        std::cout << "Changed directory to: " << fs::current_path() << std::endl;
    } else {
        std::cout << "Invalid directory path!" << std::endl;
    }
}

void navigateBack() {
    fs::current_path(fs::current_path().parent_path());
    std::cout << "Moved back to: " << fs::current_path() << std::endl;
}

void navigateHome() {
    const char* homeDir = getenv("USERPROFILE"); // Windows home directory

    if (homeDir) {
        fs::current_path(homeDir);
        std::cout << "Returned to home directory: " << fs::current_path() << std::endl;
    } else {
        std::cout << "Home directory not found!" << std::endl;
    }
}

void createFile(const std::string& filename) {
    std::ofstream file(filename);
    if (file) {
        std::cout << "File created: " << filename << std::endl;
    } else {
        std::cout << "Failed to create file!" << std::endl;
    }
}

void deleteFile(const std::string& filename) {
    if (fs::remove(filename)) {
        std::cout << "File deleted: " << filename << std::endl;
    } else {
        std::cout << "Failed to delete file!" << std::endl;
    }
}
