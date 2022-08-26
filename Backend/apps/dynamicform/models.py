from django.utils import timezone

from apps.contactinfo.models import ContactInfoModel

from django.db import models


class TVSizeModel(models.Model):
    title = models.CharField(
        max_length=25,
        help_text="TV title (size). Max 25 characters. Blank and Null are allowed.",
        blank=True,
        null=True
    )

    description = models.CharField(
        max_length=50,
        help_text="TV description (size). Max 50 characters. Blank and Null are allowed.",
        blank=True,
        null=True
    )

    size = models.CharField(
        max_length=10,
        help_text="TV size in inches (size). Max 10 characters"
    )

    price = models.CharField(
        max_length=10,
        help_text="TV price in usd (size). Max 10 characters"
    )

    img = models.ImageField(
        upload_to='tv_size/',
        blank=True, null=True
    )

    created = models.DateTimeField(
        'Created',
        default=timezone.now,
        help_text="Created",
    )

    updated = models.DateTimeField(
        'Updated',
        auto_now=True,
        help_text="Updated",
    )

    order = models.PositiveIntegerField(
        'Orden',
        default=0,
        help_text="Orden de visualización",
        blank=True, null=True,
    )

    def __str__(self):
        return f"{self.id} - {self.title} - {self.description} - {self.size} - {self.price}"

    class Meta:
        verbose_name = "TV Size"
        verbose_name_plural = "TV Size"
        db_table = "apps_tv_size"
        ordering = ['order', 'id']


class TVSurfaceModel(models.Model):
    title = models.CharField(
        max_length=25,
        help_text="TV title (surface). Max 25 characters. Blank and Null are allowed.",
        blank=True,
        null=True
    )

    description = models.CharField(
        max_length=50,
        help_text="TV description (surface). Max 50 characters. Blank and Null are allowed.",
        blank=True,
        null=True
    )

    price = models.CharField(
        max_length=10,
        help_text="TV price (surface). Max 10 characters.",
    )

    img = models.ImageField(
        upload_to='tv_surface/',
        blank=True, null=True
    )

    created = models.DateTimeField(
        'Created',
        default=timezone.now,
        help_text="Created",
    )

    updated = models.DateTimeField(
        'Updated',
        auto_now=True,
        help_text="Updated",
    )

    order = models.PositiveIntegerField(
        'Orden',
        default=0,
        help_text="Orden de visualización",
        blank=True, null=True,
    )

    def __str__(self):
        return f"{self.id} - {self.title} - {self.description} - {self.price}"

    class Meta:
        verbose_name = "TV Surface"
        verbose_name_plural = "TV Surface"
        db_table = "apps_tv_surface"
        ordering = ['order', 'id']


class TVWallMountModel(models.Model):
    title = models.CharField(
        max_length=25,
        help_text="TV title (wall-mount). Max 25 characters. Blank and Null are allowed.",
        blank=True,
        null=True
    )

    description = models.CharField(
        max_length=50,
        help_text="TV description (wall-mount). Max 50 characters. Blank and Null are allowed.",
        blank=True,
        null=True
    )

    price = models.CharField(
        max_length=10,
        help_text="TV price (wall-mount). Max 10 characters.",
    )

    img = models.ImageField(
        upload_to='tv_wall_mount/',
        blank=True, null=True
    )

    created = models.DateTimeField(
        'Created',
        default=timezone.now,
        help_text="Created",
    )

    updated = models.DateTimeField(
        'Updated',
        auto_now=True,
        help_text="Updated",
    )

    order = models.PositiveIntegerField(
        'Orden',
        default=0,
        help_text="Orden de visualización",
        blank=True, null=True,
    )

    def __str__(self):
        return f"{self.id} - {self.title} - {self.description} - {self.price}"

    class Meta:
        verbose_name = "TV Wall Mount"
        verbose_name_plural = "TV Wall Mount"
        db_table = "apps_tv_wall_mount"
        ordering = ['order', 'id']


class TVHandleCordsModel(models.Model):
    title = models.CharField(
        max_length=25,
        help_text="TV title (handleCords). Max 25 characters. Blank and Null are allowed.",
        blank=True,
        null=True
    )

    description = models.CharField(
        max_length=50,
        help_text="TV description (handleCords). Max 50 characters. Blank and Null are allowed.",
        blank=True,
        null=True
    )

    price = models.CharField(
        max_length=10,
        help_text="TV price (handleCords). Max 10 characters.",
    )

    created = models.DateTimeField(
        'Created',
        default=timezone.now,
        help_text="Created",
    )

    updated = models.DateTimeField(
        'Updated',
        auto_now=True,
        help_text="Updated",
    )

    order = models.PositiveIntegerField(
        'Orden',
        default=0,
        help_text="Orden de visualización",
        blank=True, null=True,
    )

    def __str__(self):
        return f"{self.id} - {self.title} - {self.description} - {self.price}"

    class Meta:
        verbose_name = "TV Handle Cords"
        verbose_name_plural = "TV Handle Cords"
        db_table = "apps_tv_handle_cords"
        ordering = ['order', 'id']


class TVOtherInstallsModel(models.Model):
    title = models.CharField(
        max_length=25,
        help_text="TV title (otherInstalls). Max 25 characters. Blank and Null are allowed.",
        blank=True,
        null=True
    )

    description = models.CharField(
        max_length=50,
        help_text="TV description (otherInstalls). Max 50 characters. Blank and Null are allowed.",
        blank=True,
        null=True
    )

    price = models.CharField(
        max_length=10,
        help_text="TV price (otherInstalls). Max 10 characters.",
    )

    img = models.ImageField(
        upload_to='tv_other_installs/',
        blank=True, null=True
    )

    created = models.DateTimeField(
        'Created',
        default=timezone.now,
        help_text="Created",
    )

    updated = models.DateTimeField(
        'Updated',
        auto_now=True,
        help_text="Updated",
    )

    order = models.PositiveIntegerField(
        'Orden',
        default=0,
        help_text="Orden de visualización",
        blank=True, null=True,
    )

    def __str__(self):
        return f"{self.id} - {self.title} - {self.description} - {self.price}"

    class Meta:
        verbose_name = "TV Other Installs"
        verbose_name_plural = "TV Other Installs"
        db_table = "apps_tv_other_installs"
        ordering = ['order', 'id']


class TVQuestionsModel(models.Model):
    title = models.CharField(
        max_length=25,
        help_text="TV title (otherInstalls). Max 25 characters. Blank and Null are allowed.",
        blank=True,
        null=True
    )

    description = models.CharField(
        max_length=50,
        help_text="TV description (otherInstalls). Max 50 characters. Blank and Null are allowed.",
        blank=True,
        null=True
    )

    price = models.CharField(
        max_length=10,
        help_text="TV price (otherInstalls). Max 10 characters.",
        blank=True, null=True
    )

    img = models.ImageField(
        upload_to='tv_questions/',
        blank=True, null=True
    )

    created = models.DateTimeField(
        'Created',
        default=timezone.now,
        help_text="Created",
    )

    updated = models.DateTimeField(
        'Updated',
        auto_now=True,
        help_text="Updated",
    )

    order = models.PositiveIntegerField(
        'Orden',
        default=0,
        help_text="Orden de visualización",
        blank=True, null=True,
    )

    def __str__(self):
        return f"{self.id} - {self.title} - {self.description} - {self.price}"

    class Meta:
        verbose_name = "TV Questions"
        verbose_name_plural = "TV Questions"
        db_table = "apps_tv_questions"
        ordering = ['order', 'id']


class TVWallMountInstallationModel(models.Model):
    """
    TV Wall Mount Installation model
    """
    HELP_TECHNICIAN_YES = 'Y'
    HELP_TECHNICIAN_NO = 'N'
    GET_DOWN_TV_YES = 'Y'
    GET_DOWN_TV_NO = 'N'

    give_help_choices = [
        (HELP_TECHNICIAN_YES, 'Yes'),
        (HELP_TECHNICIAN_NO, 'No'),
    ]

    get_down_choices = [
        (GET_DOWN_TV_YES, 'Yes'),
        (GET_DOWN_TV_NO, 'No'),
    ]

    user_info = models.OneToOneField(
        ContactInfoModel,
        help_text="User info",
        on_delete=models.DO_NOTHING,
    )
    
    helpTechnician = models.CharField(
        choices=give_help_choices,
        max_length=1,
        help_text="Help technician. Max 1 character. choices: Y or N.",
    )

    takeDownTV = models.CharField(
        choices=get_down_choices,
        max_length=1,
        help_text="Take down TV. Max 1 character. choices: Y or N.",
    )

    comments = models.TextField(
        help_text="Comments. Blank and Null are allowed.",
        blank=True,
        null=True
    )

    TVsize = models.ForeignKey(
        TVSizeModel,
        on_delete=models.CASCADE,
        help_text="TV size. Required. Foreign Key to TVSizeModel."
    )

    TVsurface = models.ForeignKey(
        TVSurfaceModel,
        on_delete=models.CASCADE,
        help_text="TV surface. Required. Foreign Key to TVSurfaceModel."
    )

    TVWallMount = models.ForeignKey(
        TVWallMountModel,
        on_delete=models.CASCADE,
        help_text="TV wall mount. Required. Foreign Key to TVWallMountModel."
    )

    TVHandleCords = models.ForeignKey(
        TVHandleCordsModel,
        on_delete=models.CASCADE,
        help_text="TV handle cords. Required. Foreign Key to TVHandleCordsModel."
    )

    TVOtherInstalations = models.ForeignKey(
        TVOtherInstallsModel,
        on_delete=models.CASCADE,
        help_text="TV other instalations. Required. Foreign Key to TVOtherInstallsModel."
    )

    otherQuestions = models.ManyToManyField(
        TVQuestionsModel,
        blank=True,
        help_text="TV other questions."
    )

    created = models.DateTimeField(
        'Created',
        default=timezone.now,
        help_text="Created",
    )

    updated = models.DateTimeField(
        'Updated',
        auto_now=True,
        help_text="Updated",
    )

    order = models.PositiveIntegerField(
        'Orden',
        default=0,
        help_text="Orden de visualización",
        blank=True, null=True,
    )

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = "Form TV Model"
        verbose_name_plural = "Form TV Model"
        db_table = "apps_tv_wall_mount_installation"
        ordering = ['order', 'id']
