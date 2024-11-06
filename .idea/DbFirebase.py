from firebase_admin import firestore

class DbFirebase:
    def __init__(self):
        self.db = firestore.client()
        self.doc_ref_user = None
        self.doc_ref_message = None
        self.doc_ref_image = None
        self.doc_ref_AIimage = None

    # Function to change the user document path based on userName
    def change_user_path(self, userName):
        self.doc_ref_user = self.db.collection("user").document(userName)

    # CRUD Functions for User

    def create_user_document(self, data):
        if self.doc_ref_user:
            self.doc_ref_user.set(data)
            print(f"User document created: {self.doc_ref_user.id}")

    def read_user_document(self):
        if self.doc_ref_user:
            doc = self.doc_ref_user.get()
            if doc.exists:
                print(f"User document read: {self.doc_ref_user.id}")
                return doc.to_dict()
            else:
                print("User document does not exist.")
                return None

    def update_user_document(self, data):
        if self.doc_ref_user:
            self.doc_ref_user.update(data)
            print(f"User document updated: {self.doc_ref_user.id}")

    def delete_user_document(self):
        if self.doc_ref_user:
            self.doc_ref_user.delete()
            print(f"User document deleted: {self.doc_ref_user.id}")

    # CRUD Functions for Subcollections (Message, Image, AI_image)

    def set_message_ref(self, message_id):
        self.doc_ref_message = self.doc_ref_user.collection("message").document(message_id)

    def set_image_ref(self, image_id):
        self.doc_ref_image = self.doc_ref_user.collection("image").document(image_id)

    def set_AIimage_ref(self, AIimage_id):
        self.doc_ref_AIimage = self.doc_ref_user.collection("AI_image").document(AIimage_id)

    # Query Functions

    # Query for users based on specific criteria (e.g., age range, location)
    def find_users_by_field_range(self, field, start_val, end_val):
        query = self.db.collection("user").where(field, ">=", start_val).where(field, "<=", end_val)
        docs = query.get()
        results = [doc.to_dict() for doc in docs]
        print(f"Users with {field} in range {start_val} to {end_val}: {results}")
        return results

    # Range query for message subcollection
    def find_messages_in_range(self, field, start_val, end_val):
        query = self.doc_ref_user.collection("message").where(field, ">=", start_val).where(field, "<=", end_val)
        docs = query.get()
        results = [doc.to_dict() for doc in docs]
        print(f"Messages with {field} in range {start_val} to {end_val}: {results}")
        return results

    # Range query for image subcollection
    def find_images_in_range(self, field, start_val, end_val):
        query = self.doc_ref_user.collection("image").where(field, ">=", start_val).where(field, "<=", end_val)
        docs = query.get()
        results = [doc.to_dict() for doc in docs]
        print(f"Images with {field} in range {start_val} to {end_val}: {results}")
        return results

    # Range query for AI_image subcollection
    def find_AIimages_in_range(self, field, start_val, end_val):
        query = self.doc_ref_user.collection("AI_image").where(field, ">=", start_val).where(field, "<=", end_val)
        docs = query.get()
        results = [doc.to_dict() for doc in docs]
        print(f"AI Images with {field} in range {start_val} to {end_val}: {results}")
        return results

    # Query for finding users by exact field value
    def find_users_by_exact_field(self, field, value):
        query = self.db.collection("user").where(field, "==", value)
        docs = query.get()
        results = [doc.to_dict() for doc in docs]
        print(f"Users with {field} == {value}: {results}")
        return results

    # Query for finding documents in message subcollection by exact field value
    def find_messages_by_exact_field(self, field, value):
        query = self.doc_ref_user.collection("message").where(field, "==", value)
        docs = query.get()
        results = [doc.to_dict() for doc in docs]
        print(f"Messages with {field} == {value}: {results}")
        return results

    # Query for finding documents in image subcollection by exact field value
    def find_images_by_exact_field(self, field, value):
        query = self.doc_ref_user.collection("image").where(field, "==", value)
        docs = query.get()
        results = [doc.to_dict() for doc in docs]
        print(f"Images with {field} == {value}: {results}")
        return results

    # Query for finding documents in AI_image subcollection by exact field value
    def find_AIimages_by_exact_field(self, field, value):
        query = self.doc_ref_user.collection("AI_image").where(field, "==", value)
        docs = query.get()
        results = [doc.to_dict() for doc in docs]
        print(f"AI Images with {field} == {value}: {results}")
        return results

    # Logging function
    def show_log(self, method, user_id, message):
        print(f"{method}: User: {user_id}, Message: {message}")
