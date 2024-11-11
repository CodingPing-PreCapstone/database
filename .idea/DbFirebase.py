import firebase_admin
from firebase_admin import credentials, firestore

class DbFirebase:
    def __init__(self):



        if not firebase_admin._apps:
            cred = credentials.Certificate("path/to/your/serviceAccountKey.json")  # 경로를 올바르게 설정하세요.
            # firebase_admin.initialize_app(cred)


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


    # Message CRUD Functions

    def set_message_ref(self, message_id):
        self.doc_ref_message = self.doc_ref_user.collection("message").document(message_id)

    def create_message_document(self, data):
        if self.doc_ref_message:
            self.doc_ref_message.set(data)
            print(f"Message document created: {self.doc_ref_message.id}")

    def read_message_document(self):
        if self.doc_ref_message:
            doc = self.doc_ref_message.get()
            if doc.exists:
                print(f"Message document read: {self.doc_ref_message.id}")
                return doc.to_dict()
            else:
                print("Message document does not exist.")
                return None

    def update_message_document(self, data):
        if self.doc_ref_message:
            self.doc_ref_message.update(data)
            print(f"Message document updated: {self.doc_ref_message.id}")

    def delete_message_document(self):
        if self.doc_ref_message:
            self.doc_ref_message.delete()
            print(f"Message document deleted: {self.doc_ref_message.id}")

    # Image CRUD Functions

    def set_image_ref(self, image_id):
        self.doc_ref_image = self.doc_ref_user.collection("image").document(image_id)

    def create_image_document(self, data):
        if self.doc_ref_image:
            self.doc_ref_image.set(data)
            print(f"Image document created: {self.doc_ref_image.id}")

    def read_image_document(self):
        if self.doc_ref_image:
            doc = self.doc_ref_image.get()
            if doc.exists:
                print(f"Image document read: {self.doc_ref_image.id}")
                return doc.to_dict()
            else:
                print("Image document does not exist.")
                return None

    def update_image_document(self, data):
        if self.doc_ref_image:
            self.doc_ref_image.update(data)
            print(f"Image document updated: {self.doc_ref_image.id}")

    def delete_image_document(self):
        if self.doc_ref_image:
            self.doc_ref_image.delete()
            print(f"Image document deleted: {self.doc_ref_image.id}")

    # AI Image CRUD Functions

    def set_AIimage_ref(self, AIimage_id):
        self.doc_ref_AIimage = self.doc_ref_user.collection("AI_image").document(AIimage_id)

    def create_AIimage_document(self, data):
        if self.doc_ref_AIimage:
            self.doc_ref_AIimage.set(data)
            print(f"AI Image document created: {self.doc_ref_AIimage.id}")

    def read_AIimage_document(self):
        if self.doc_ref_AIimage:
            doc = self.doc_ref_AIimage.get()
            if doc.exists:
                print(f"AI Image document read: {self.doc_ref_AIimage.id}")
                return doc.to_dict()
            else:
                print("AI Image document does not exist.")
                return None

    def update_AIimage_document(self, data):
        if self.doc_ref_AIimage:
            self.doc_ref_AIimage.update(data)
            print(f"AI Image document updated: {self.doc_ref_AIimage.id}")

    def delete_AIimage_document(self):
        if self.doc_ref_AIimage:
            self.doc_ref_AIimage.delete()
            print(f"AI Image document deleted: {self.doc_ref_AIimage.id}")



    # Logging function
    def show_log(self, method, user_id, message):
        print(f"{method}: User: {user_id}, Message: {message}")
