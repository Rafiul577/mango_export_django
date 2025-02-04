from django.db import models

class MangoExport(models.Model):
    variety = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Use order_id as the sole primary key; do not allow null values.
    order_id = models.IntegerField(primary_key=True, blank=True)

    def save(self, *args, **kwargs):
        # Assign order_id if not set.
        if self.order_id is None:
            last_entry = MangoExport.objects.order_by('-order_id').first()
            self.order_id = 1 if last_entry is None else last_entry.order_id + 1
        super().save(*args, **kwargs)

    @staticmethod
    def reorder_ids():
        """Reassign sequential order_ids based on current records."""
        mangoes = MangoExport.objects.order_by('order_id')
        for index, mango in enumerate(mangoes, start=1):
            if mango.order_id != index:
                mango.order_id = index
                # Save without using update_fields to avoid field lookup issues.
                mango.save()

    def __str__(self):
        return self.variety
