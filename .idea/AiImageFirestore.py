from FirestoreInterface import FirestoreInterface


# AIImageFirestore 클래스
class AIImageFirestore(FirestoreInterface):
    def __init__(self):
        super().__init__('user/user/AI_image')

    def create_ai_image(self, data):
        image_id = self.create_document(data)
        self._ensure_limit()
        return image_id

    def get_ai_image(self, doc_id):
        return self.read_document(doc_id)

    def update_ai_image(self, doc_id, data):
        return self.update_document(doc_id, data)

    def delete_ai_image(self, doc_id):
        return self.delete_document(doc_id)

    def list_ai_images(self):
        return self.get_all_documents()

    def _ensure_limit(self):
        """AI 이미지가 10개 이상일 경우 오래된 순으로 삭제합니다."""
        ai_images = list(self.collection_ref.order_by("sentTime").stream())
        if len(ai_images) > 10:
            for doc in ai_images[:-10]:  # 오래된 순으로 초과된 문서 삭제
                doc.reference.delete()
