CREATE TABLE `Servicio` (
  `Servicio_ID` INT,
  `Area_ID` INT,
  `Nombre_Servicio` VARCHAR(50),
  PRIMARY KEY (`Servicio_ID`)
);

CREATE TABLE `Clientes` (
  `Cliente_ID` INT,
  `Nombre_Cliente` VARCHAR(100),
  `Apellido_Cliente` VARCHAR(100),
  `Cel_Cliente` INT,
  `Correo_Cliente` VARCHAR(200),
  `Direccion_Cliente` VARCHAR(100),
  `Identificacion_Cliente` INT,
  PRIMARY KEY (`Cliente_ID`)
);

CREATE TABLE `Empleado` (
  `Empleado_ID` INT,
  `Area_ID` VARCHAR(50),
  `Nombre_Empleado` VARCHAR (50),
  `Apellido_Empleado` VARCHAR(50),
  `Cedula_Empleado` INT,
  `Numero_Empleado` INT,
  `Estado_Empleado` BOOL,
  `Fecha_Contratacion` DATE,
  PRIMARY KEY (`Empleado_ID`)
);

CREATE TABLE `Area` (
  `Area_ID` INT,
  `Nombre_Area` VARCHAR(50),
  `Porcentaje_comision` INT,
  PRIMARY KEY (`Area_ID`)
);

CREATE TABLE `Orden_trabajo` (
  `Orden_ID` INT,
  `Cliente_ID` INT,
  `Empleado_ID` INT,
  `Servicio_ID` INT,
  `Estado` VARCHAR(50),
  `Fecha` DATE,
  `Marca_Vehiculo` VARCHAR(50),
  `Placa_Vehiculo` VARCHAR(50),
  `Diagnostico` VARCHAR(200),
  `Area_ID` INT,
  PRIMARY KEY (`Orden_ID`),
  FOREIGN KEY (`Cliente_ID`) REFERENCES `Clientes`(`Cliente_ID`),
  FOREIGN KEY (`Empleado_ID`) REFERENCES `Empleado`(`Empleado_ID`),
  FOREIGN KEY (`Servicio_ID`) REFERENCES `Servicio`(`Servicio_ID`),
  FOREIGN KEY (`Area_ID`) REFERENCES `Area`(`Area_ID`)
);

CREATE TABLE `Servicios_Vendidos` (
  `Servicio_ID` INT,
  `Orden_ID` INT,
  `Precio_Servicio` INT,
  `Fecha` DATE,
  FOREIGN KEY (`Servicio_ID`) REFERENCES `Servicio`(`Servicio_ID`),
  FOREIGN KEY (`Orden_ID`) REFERENCES `Orden_trabajo`(`Servicio_ID`)
);

CREATE TABLE `Remision` (
  `Remision_ID` INT,
  `Orden_ID` INT,
  `Cliente_ID` INT,
  `Fecha` DATE,
  `Estado` VARCHAR(50),
  PRIMARY KEY (`Remision_ID`),
  FOREIGN KEY (`Orden_ID`) REFERENCES `Orden_trabajo`(`Orden_ID`),
  FOREIGN KEY (`Cliente_ID`) REFERENCES `Clientes`(`Cliente_ID`)
);

CREATE TABLE `Proveedores` (
  `Proveedor_ID` INT,
  `Identificacion_Proveedor` INT,
  `Telefono_Proveedor` INT,
  `Nombre_Proveedor` VARCHAR(100),
  `Direccion_Proveedor` VARCHAR(100),
  PRIMARY KEY (`Proveedor_ID`)
);

CREATE TABLE `Repuestos` (
  `Repuesto_ID` INT,
  `Proveedor_ID` INT,
  `Nombre_Repuesto` VARCHAR(50),
  `Precio_Compra` INT,
  `Precio_Venta` INT,
  `Referencia_Articulo` VARCHAR(100),
  `Cantidad` INT,
  `Fecha_Compra` DATE,
  `Estado` VARCHAR(50),
  PRIMARY KEY (`Repuesto_ID`),
  FOREIGN KEY (`Proveedor_ID`) REFERENCES `Proveedores`(`Proveedor_ID`)
);

CREATE TABLE `Orden_trabajo_Repuesto` (
  `Orden_ID` INT,
  `Repuesto_ID` INT,
  `Fecha` DATE,
  FOREIGN KEY (`Repuesto_ID`) REFERENCES `Repuestos`(`Repuesto_ID`),
  FOREIGN KEY (`Orden_ID`) REFERENCES `Orden_trabajo`(`Orden_ID`)
);

CREATE TABLE `Factura` (
  `Factura_ID` INT,
  `Orden_ID` INT,
  `Cliente_ID` INT,
  `Fecha` DATE,
  `Estado` VARCHAR(50),
  PRIMARY KEY (`Factura_ID`),
  FOREIGN KEY (`Orden_ID`) REFERENCES `Orden_trabajo`(`Orden_ID`),
  FOREIGN KEY (`Cliente_ID`) REFERENCES `Clientes`(`Cliente_ID`)
);

CREATE TABLE `Comision` (
  `Comision_ID` INT,
  `Factura_ID` INT,
  `Remision_ID` INT,
  `Empleado_ID` INT,
  `Porcentaje_Comision` INT,
  `Area_ID` INT,
  PRIMARY KEY (`Comision_ID`),
  FOREIGN KEY (`Empleado_ID`) REFERENCES `Empleado`(`Empleado_ID`),
  FOREIGN KEY (`Remision_ID`) REFERENCES `Remision`(`Remision_ID`),
  FOREIGN KEY (`Factura_ID`) REFERENCES `Factura`(`Factura_ID`)
);

CREATE TABLE `Orden_trabajo_Empleado` (
  `Orden_ID` INT,
  `Empleado_ID` INT,
  `Fecha` DATE,
  FOREIGN KEY (`Orden_ID`) REFERENCES `Orden_trabajo`(`Empleado_ID`),
  FOREIGN KEY (`Empleado_ID`) REFERENCES `Empleado`(`Empleado_ID`)
);

CREATE TABLE `Cotizaciones` (
  `Cotizacion_ID` INT,
  `Cliente_ID` INT,
  `Repuesto_ID` INT,
  `Fecha` DATE,
  `Marca_Vehiculo` VARCHAR(50),
  `Placa_Vehiculo` VARCHAR(50),
  `Descripcion` VARCHAR(200),
  `Estado` VARCHAR(50),
  PRIMARY KEY (`Cotizacion_ID`),
  FOREIGN KEY (`Cliente_ID`) REFERENCES `Clientes`(`Cliente_ID`),
  FOREIGN KEY (`Repuesto_ID`) REFERENCES `Repuestos`(`Repuesto_ID`)
);

CREATE TABLE `Semana` (
  `Semana_ID` INT,
  `Fecha_inicio` DATE,
  `Fecha_fin` DATE,
  PRIMARY KEY (`Semana_ID`)
);

CREATE TABLE `Areas_incluidas` (
  `Orden_ID` INT,
  `Area_ID` INT,
  `Fecha` DATE,
  FOREIGN KEY (`Orden_ID`) REFERENCES `Orden_trabajo`(`Orden_ID`),
  FOREIGN KEY (`Area_ID`) REFERENCES `Area`(`Area_ID`)
);

CREATE TABLE `Pagos_empleados` (
  `Pago_empleado_ID` INT,
  `Empleado_ID` INT,
  `Semana_ID` INT,
  `Monto_total` INT,
  `Detalle_orden_trabajo` VARCHAR(50),
  `Descuento` INT,
  PRIMARY KEY (`Pago_empleado_ID`),
  FOREIGN KEY (`Semana_ID`) REFERENCES `Semana`(`Semana_ID`),
  FOREIGN KEY (`Empleado_ID`) REFERENCES `Empleado`(`Empleado_ID`)
);

CREATE TABLE `Fechas_Importantes` (
  `Fecha` VARCHAR(100),
  `Evento` VARCHAR(200)
);


