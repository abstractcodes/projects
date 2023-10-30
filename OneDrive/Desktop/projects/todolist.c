#include <stdio.h>
#include <stdlib.h>

// Define the structure for tasks
typedef struct {
    int unique_id;
    char description[100];
} Task;

int main(int argc, char *argv[]) {
    FILE *file;
    Task task;
    int number = 0; // Initialize the number to 0

    // Open the file in read mode to check if it exists
    file = fopen("tasks.txt", "r");
    if (file == NULL) {
        printf("No tasks found.\n");
    } else {
        fclose(file);
    }

    // Prompt the user to enter a new task
    Task new_task;
    printf("Enter new task:\n");
    scanf(" %[^\n]", new_task.description); // Read the entire line

    // Assign a unique ID
    new_task.unique_id = number + 1;

    // Open the file in append mode to add the new task
    file = fopen("tasks.txt", "a");
    fwrite(&new_task, sizeof(Task), 1, file);
    fclose(file);

    // Open the file again to display the tasks
    file = fopen("tasks.txt", "r");
    if (file == NULL) {
        printf("No tasks found.\n");
        return 1;
    }

    printf("Tasks:\n");
    while (fread(&task, sizeof(Task), 1, file)) {
        printf("Task ID: %d, Description: %s\n", task.unique_id, task.description);
    }
    fclose(file);

    int taskToRemove; // Declare a variable to store the ID of the task to remove

    printf("Enter the ID of the task to remove: ");
    scanf("%d", &taskToRemove);
    int delete_element = 1;
    if (delete_element == 0){
    // Create a temporary file to rewrite the tasks without the one to remove
    FILE *tempFile = fopen("temp.txt", "w");
    file = fopen("tasks.txt", "r");

    while (fread(&task, sizeof(Task), 1, file)) {
        if (task.unique_id != taskToRemove) {
            fwrite(&task, sizeof(Task), 1, tempFile);
        }
    }

    fclose(file);
    fclose(tempFile);

    // Rename the temporary file to the original file to apply changes
    remove("tasks.txt");
    rename("temp.txt", "tasks.txt");
    }
}
