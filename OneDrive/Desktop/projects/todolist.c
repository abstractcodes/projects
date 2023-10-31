#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define the structure for tasks
typedef struct {
    int unique_id;
    char description[100];
} Task;

// Function to serialize a task struct into a string
void serializeTask(char buffer[], Task task) {
    snprintf(buffer, 200, "%d %s", task.unique_id, task.description);
}

// Function to deserialize a string into a task struct
void deserializeTask(const char buffer[], Task *task) {
    sscanf(buffer, "%d %[^\n]", &task->unique_id, task->description);
}

int main(int argc, char *argv[]) {
    FILE *file;
    int number = 0;
    char buffer[200]; // Allocate a buffer for serialization

    // Open the file in read mode to check if it exists
    file = fopen("tasks.txt", "r");
    if (file == NULL) {
        printf("No tasks found.\n");
    } else {
        fclose(file);
    }
    int continue_loop = 1;
    int choice;
    while (continue_loop==1){
    printf("Please enter 1 for inserting a new task or 2 for deleting a task: ");
    scanf("%d", &choice);
    // Prompt the user to enter a new task
    if (choice==1){
    Task new_task;
    printf("Enter new task:\n");
    scanf(" %[^\n]", new_task.description); // Read the entire line

    // Assign a unique ID
    new_task.unique_id = number + 1;
    number += 1;

    // Serialize the new task and write it to the file
    serializeTask(buffer, new_task);

    file = fopen("tasks.txt", "a");
    fprintf(file, "%s\n", buffer);
    fclose(file);

    // Open the file again to display the tasks
    file = fopen("tasks.txt", "r");
    if (file == NULL) {
        printf("No tasks found.\n");
        return 1;
    }

    printf("Tasks:\n");
    while (fgets(buffer, sizeof(buffer), file)) {
        Task task;
        deserializeTask(buffer, &task);
        printf("Task ID: %d, Description: %s\n", task.unique_id, task.description);
    }
    fclose(file);}
    if (choice==2){
    int taskToRemove; // Declare a variable to store the ID of the task to remove

    printf("Enter the ID of the task to remove: ");
    scanf("%d", &taskToRemove);

    // Create a temporary file to rewrite the tasks without the one to remove
    FILE *tempFile = fopen("temp.txt", "w");
    file = fopen("tasks.txt", "r");

    while (fgets(buffer, sizeof(buffer), file)) {
        Task task;
        deserializeTask(buffer, &task);
        if (task.unique_id != taskToRemove) {
            serializeTask(buffer, task);
            fprintf(tempFile, "%s\n", buffer);
        }
    }

    fclose(file);
    fclose(tempFile);

    // Rename the temporary file to the original file to apply changes
    remove("tasks.txt");
    rename("temp.txt", "tasks.txt");
        // Open the file again to display the tasks
    file = fopen("tasks.txt", "r");
    if (file == NULL) {
        printf("No tasks found.\n");
        return 1;
    }

    printf("Tasks:\n");
    while (fgets(buffer, sizeof(buffer), file)) {
        Task task;
        deserializeTask(buffer, &task);
        printf("Task ID: %d, Description: %s\n", task.unique_id, task.description);
    }
    fclose(file);
    }
    printf("Enter 1 for continuing the process: ");
    scanf("%d",&continue_loop);
    }
}
