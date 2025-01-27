from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Seeds the database with sample listings, bookings, and reviews'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Seeding database...'))

        # Create Listings
        for _ in range(10):
            listing = Listing.objects.create(
                title=fake.company(),
                description=fake.text(),
                price_per_night=random.uniform(50, 500),
                location=fake.city()
            )
            self.stdout.write(self.style.SUCCESS(f'Created listing: {listing.title}'))

            # Create Bookings for each listing
            for _ in range(5):
                Booking.objects.create(
                    listing=listing,
                    guest_name=fake.name(),
                    guest_email=fake.email(),
                    check_in=fake.date_this_year(),
                    check_out=fake.date_this_year(),
                    total_price=random.uniform(100, 2000),
                )

            # Create Reviews for each listing
            for _ in range(3):
                Review.objects.create(
                    listing=listing,
                    reviewer_name=fake.name(),
                    rating=random.randint(1, 5),
                    comment=fake.text()
                )

        self.stdout.write(self.style.SUCCESS('Database seeding completed successfully.'))
