class ReviewItem:
    def __init__(self, text, rating):
        self.text = text
        self.rating = rating
    
    def __str__(self):
        return f"Оценка: {self.rating} звездички - {self.text}"


class HighRatingReviewIterator:
    def __init__(self, reviews):
        self.reviews = reviews
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.index < len(self.reviews):
            review = self.reviews[self.index]
            self.index += 1
            if review.rating >= 4:
                return review
        raise StopIteration


if __name__ == "__main__":
    reviews = [
        ReviewItem("Много добро продуктче!", 5),
        ReviewItem("Добре.", 4),
        ReviewItem("Mid.", 3),
        ReviewItem("Не е добре положението.", 2),
        ReviewItem("Много лошо, не си заслуждава.", 1),
        ReviewItem("Препоръчвам, YES!", 5),
        ReviewItem("Добра покупка.", 4)
    ]
    
    print("Всички ревюта:")
    for review in reviews:
        print(review)
    
    print("\nСамо ревюта с 4 или 5 звезди:")
    high_rating_iterator = HighRatingReviewIterator(reviews)
    for review in high_rating_iterator:
        print(review)
