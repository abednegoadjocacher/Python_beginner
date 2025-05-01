class TextEditor:
    def _init(self):
        self.undo_stack = []  # Stack to store previous states
        self.redo_stack = []  # Stack to store undone states       
        self.current_text = ""  # Current text in the editor   
    def display_menu(self):
        print("\n--- Text Editor Menu ---")      
        print("1. Enter Text")        
        print("2. Undo")       
        print("3. Redo")       
        print("4. Exit")    
    def edit_text(self):       
        print(f"\nCurrent Text: {self.current_text}")      
        new_text = input("Enter new text: ")        
        self.undo_stack.append(self.current_text)  # Save current state for undo       
        self.current_text = new_text  # Update text       
        self.redo_stack.clear()  # Clear redo stack       
        print("Text updated successfully!")   
    def undo(self):       
        if not self.undo_stack:          
            print("Nothing to undo!")          
            return self.redo_stack.append(self.current_text)  # Save current state for redo
        self.current_text = self.undo_stack.pop()  # Restore the previous state        
        print(f"Undo successful! Current Text: {self.current_text}")
    def redo(self):        
        if not self.redo_stack:          
            print("Nothing to redo!")           
            return self.undo_stack.append(self.current_text)  # Save current state for undo       
        self.current_text = self.redo_stack.pop()  # Restore the next state        
        print(f"Redo successful! Current Text: {self.current_text}")    
    def run(self):      
        while True:           
            self.display_menu()
            choice = input("\nEnter your choice (1-4): ")
            if choice == "1":
               self.edit_text()
            elif choice == "2":              
                self.undo()
            elif choice == "3":
                self.redo()
            elif choice == "4":
                print("Exiting text editor. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
            if __name_ == "_main_":
                editor = TextEditor()
                editor.run()