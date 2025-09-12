from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
   
    # Create a regular user
    # ------------------------------
    def create_user(self, username, email, phone_no=None, weight=None, age=None, password=None):
        # Ensure a username is provided
        if not username:
            raise ValueError("Users must have a username")

        # Build the user object with the given fields
        user = self.model(
            username=username,
            email=email,
            phone_no=phone_no,
            weight=weight,
            age=age
        )
    
        # Set (hash) the password securely
        user.set_password(password)

        # Save the user to the database using the default DB
        user.save(using=self._db)
        return user


    # Create a superuser (admin)
    # ------------------------------
    def create_superuser(self, username, email, phone_no=None, weight=None, age=None, password=None):
        # First, create a normal user with the provided fields
        user = self.create_user(
            username=username,
            email=email,
            phone_no=phone_no,
            weight=weight,
            age=age,
            password=password
        )

        # Grant admin privileges
        user.is_staff = True   # Can log into admin site
        user.is_superuser = True  # Has all permissions
        user.save(using=self._db)
        return user
