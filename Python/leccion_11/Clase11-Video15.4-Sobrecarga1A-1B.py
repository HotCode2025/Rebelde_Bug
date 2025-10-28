''' La sobrecarga de un operador significa que un operador
puede comportarse de diferentes formas. Depende si trabaja con 
tipos string, enteros o listas, por ejemplo. '''

a = 3
b = 5
print(a + b)


a = 'Hola '
b = 'Mundo'
print(a + b)


a = [3, 4, 5]
b = [6, 7, 8, 9]
print(a + b)

''' Se puede probar que funciona distinto para todos estos casos,
Esta es la lista de metodos segun el operador que queramos sobrecargar (eso en python)

Operador Aritmetico                  Magic Method
+                                   _add_(self, other)
-                                   _sub_(self, other)
*                                   _mul_(self, other)
/                                   _truediv_(self, other)
//                                  _floordiv_(self, other)
%                                   _mod_(self, other)
**                                  _pow_(self, other)

Operador Comparacion                 
<                                   _lt_(self, other)
>                                   _gt_(self, other)
<=                                  _le_(self, other)
>=                                  _ge_(self, other)
==                                  _eq_(self, other)
!=                                  _ne_(self, other)

Operador Asignacion (compuestos)                 
-=                                   _isub_(self, other)
+=                                  _iadd_(self, other)
*=                                  _imul_(self, other)
/=                                  _idiv_(self, other)
//=                                 _ifloordiv_(self, other)
%=                                  _imod_(self, other)
**=                                 _ipow_(self, other)

Operador Unarios                  
-                                   _neg_(self, other)
+                                  _pos_(self, other)
~                                  _invert_(self, other)

'''