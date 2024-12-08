class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # List to store all pet instances

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)  # Add pet to the all list
        if owner:
            owner.add_pet(self)  # Automatically add this pet to the owner's list

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_list = []

    def pets(self):
        """Return all pets belonging to this owner"""
        return self.pets_list

    def add_pet(self, pet):
        """Add a pet to the owner's pets list"""
        if isinstance(pet, Pet):
            self.pets_list.append(pet)
            pet.owner = self
        else:
            raise Exception("The pet must be an instance of Pet.")

    def get_sorted_pets(self):
        """Return a sorted list of pets by name"""
        return sorted(self.pets_list, key=lambda pet: pet.name)
