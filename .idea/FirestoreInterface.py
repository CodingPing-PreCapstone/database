from firebase_admin import firestore

class FirestoreInterface:
    def __init__(self, collection_path):
        self.collection_ref = firestore.client().collection(collection_path)

    def create_document(self, data):
        doc_ref = self.collection_ref.document()
        doc_ref.set(data)
        return doc_ref.id

    def read_document(self, doc_id):
        doc_ref = self.collection_ref.document(doc_id)
        doc = doc_ref.get()
        return doc.to_dict() if doc.exists else None

    def update_document(self, doc_id, data):
        doc_ref = self.collection_ref.document(doc_id)
        doc_ref.update(data)
        return doc_ref.id

    def delete_document(self, doc_id):
        doc_ref = self.collection_ref.document(doc_id)
        doc_ref.delete()
        return doc_id

    def get_all_documents(self):
        docs = self.collection_ref.stream()
        return [doc.to_dict() for doc in docs]




