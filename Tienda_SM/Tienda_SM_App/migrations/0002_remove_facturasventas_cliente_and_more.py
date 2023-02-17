# Generated by Django 4.1.2 on 2022-10-18 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tienda_SM_App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facturasventas',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='facturaventalinea',
            name='factura',
        ),
        migrations.RemoveField(
            model_name='facturaventalinea',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='pagoproveedores',
            name='proveedor',
        ),
        migrations.RemoveField(
            model_name='pedidos',
            name='idProducto',
        ),
        migrations.RemoveField(
            model_name='pedidos',
            name='proveedor',
        ),
        migrations.RemoveField(
            model_name='productos',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='productospedidos',
            name='pedido',
        ),
        migrations.RemoveField(
            model_name='productospedidos',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='productospedidos',
            name='proveedor',
        ),
        migrations.RemoveField(
            model_name='ventas',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='ventas',
            name='factura',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Clientes',
        ),
        migrations.DeleteModel(
            name='FacturasVentas',
        ),
        migrations.DeleteModel(
            name='FacturaVentaLinea',
        ),
        migrations.DeleteModel(
            name='PagoProveedores',
        ),
        migrations.DeleteModel(
            name='Pedidos',
        ),
        migrations.DeleteModel(
            name='Productos',
        ),
        migrations.DeleteModel(
            name='ProductosPedidos',
        ),
        migrations.DeleteModel(
            name='Proveedores',
        ),
        migrations.DeleteModel(
            name='Ventas',
        ),
    ]
