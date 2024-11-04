from FirestoreInterface import FirestoreInterface


# LastestImageFirestore 클래스
class LastestImageFirestore(FirestoreInterface):
    def __init__(self):
        super().__init__('user/user/lastest_image')

    def create_lastest_image(self, data):
        image_id = self.create_document(data)
        self._ensure_limit()
        return image_id

    def get_lastest_image(self, doc_id):
        return self.read_document(doc_id)

    def update_lastest_image(self, doc_id, data):
        return self.update_document(doc_id, data)

    def delete_lastest_image(self, doc_id):
        return self.delete_document(doc_id)

    def list_lastest_images(self):
        return self.get_all_documents()

    def _ensure_limit(self):
        """최신 이미지가 10개 이상일 경우 오래된 순으로 삭제합니다."""
        images = list(self.collection_ref.order_by("date").stream())
        if len(images) > 10:
            for doc in images[:-10]:  # 오래된 순으로 초과된 문서 삭제
                doc.reference.delete()
