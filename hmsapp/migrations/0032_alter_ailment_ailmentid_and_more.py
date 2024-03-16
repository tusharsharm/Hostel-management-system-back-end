# Generated by Django 4.2.6 on 2024-03-14 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmsapp', '0031_remove_student_user_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ailment',
            name='AilmentID',
            field=models.AutoField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='department',
            name='departmentID',
            field=models.AutoField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='healthrecord',
            name='healthId',
            field=models.AutoField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='HospitalID',
            field=models.AutoField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='hospitalvisit',
            name='VisitID',
            field=models.AutoField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='hostelasset',
            name='AssetID',
            field=models.AutoField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='MedicineID',
            field=models.AutoField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='necessitystoreitem',
            name='ItemID',
            field=models.AutoField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='OrderID',
            field=models.AutoField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='ReservationID',
            field=models.AutoField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='room',
            name='RoomID',
            field=models.AutoField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='roomleader',
            name='RoomLeaderID',
            field=models.AutoField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
