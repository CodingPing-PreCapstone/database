from FirestoreInterface import FirestoreInterface



# MessageFirestore 클래스
class MessageFirestore(FirestoreInterface):
    def __init__(self):
        super().__init__('user/user/message')

    def create_message(self, data):
        message_id = self.create_document(data)
        self._ensure_limit()
        return message_id

    def get_message(self, doc_id):
        return self.read_document(doc_id)

    def update_message(self, doc_id, data):
        return self.update_document(doc_id, data)

    def delete_message(self, doc_id):
        return self.delete_document(doc_id)

    def list_messages(self):
        return self.get_all_documents()

    def _ensure_limit(self):
        """문자가 10개 이상일 경우 오래된 순으로 삭제합니다."""
        messages = list(self.collection_ref.order_by("sentTime").stream())
        if len(messages) > 10:
            for doc in messages[:-10]:  # 오래된 순으로 초과된 문서 삭제
                doc.reference.delete()