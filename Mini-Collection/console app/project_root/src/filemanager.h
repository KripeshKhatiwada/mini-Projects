#ifndef FILEMANAGER_H
#define FILEMANAGER_H

#include <string>  // For std::string
#include <iostream> // For standard I/O operations

void showCurrentDirectory();
void navigateToDirectory(const std::string& path);
void navigateBack();
void navigateHome();
void createFile(const std::string& filename);
void deleteFile(const std::string& filename);

#endif // FILEMANAGER_H
