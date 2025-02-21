from database.db import db

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True, nullable=False)
    balance = db.Column(db.Float, default=0.0)

    @staticmethod
    def get_account_by_user_id(user_id):
        return Account.query.filter_by(user_id=user_id).first()

    def deposit(self, amount):
        self.balance += amount
        db.session.commit()

    def withdraw(self, amount):
        self.balance -= amount
        db.session.commit()

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account ID: {self.id}, User ID: {self.user_id}, Balance: Rs {self.balance:.2f}"