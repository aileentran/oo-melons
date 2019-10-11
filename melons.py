"""Classes for melon orders."""
class AbstractMelonOrder():

    def __init__(self,species,qty):
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5

        if self.species == 'christmas melon':
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == 'international' and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    
    def __init__(self,species,qty):
        super().__init__(species,qty)
        self.order_type = "domestic"
        self.tax = 0.08


   

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    
    def __init__(self,species,qty,country_code):
        """Initialize melon order attributes."""
        super().__init__(species,qty)
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

        
    # def set_price(self):
    #     total = super().get_total()
    #     if self.qty < 10:
    #         total += 3
    #     return total

   

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """Class for melon orders from the government!"""

    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.order_type = "government order"
        self.tax = 0
        self.passed_inspection = False

    def mark_inspection(self):
        self.passed_inspection = True

    