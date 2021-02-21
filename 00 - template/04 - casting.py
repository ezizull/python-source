# casting: merubah dari satu tipe ke tipe lain
# tipe data: str, bool, int, float

## INTEGER
print("=== INTEGER ===")
data_int = 9;
print("data = ", data_int, ", type =",type(data_int))

data_str   = str(data_int)
data_float = float(data_int)
data_bool  = bool(data_int) # klo 0 akan FALSE, klo tidak akan TRUE
print("\t. data = ", data_str, ", type =",type(data_str))
print("\t. data = ", data_float, ", type =",type(data_float))
print("\t. data = ", data_bool, ", type =",type(data_bool), ",\n")

## FLOAT
print("=== FLOAT ===")
data_float = 9.5;
print("data = ", data_float, ", type =",type(data_float))

data_str   = str(data_float)
data_int   = int(data_float) # akan dibulatkan kebawah pasti jadi "9.0"
data_bool  = bool(data_float) # klo 0 akan FALSE, klo tidak akan TRUE
print("\t. data = ", data_str, ", type =",type(data_str))
print("\t. data = ", data_int, ", type =",type(data_int))
print("\t. data = ", data_bool, ", type =",type(data_bool), ",\n")

## BOOLEAN
print("=== BOOLEAN ===")
data_bool = False;
print("data = ", data_bool, ", type =",type(data_bool))

data_str   = str(data_bool)
data_int   = int(data_bool) 
data_float  = float(data_bool)
print("\t. data = ", data_str, ", type =",type(data_str))
print("\t. data = ", data_int, ", type =",type(data_int))
print("\t. data = ", data_float, ", type =",type(data_float), ",\n")

## STRING
print("=== STRING ===")
data_str = "10";
print("data = ", data_str, ", type =",type(data_str))

data_int   = int(data_str) # "ucup" = ERROR - Harus ( "10" ) ato ERROR
data_float  = float(data_str)
data_bool   = bool(data_str) # ( "0" ) = TRUE - Harus ( "" ) baru "FALSE
print("\t. data = ", data_int, ", type =",type(data_int))
print("\t. data = ", data_float, ", type =",type(data_float))
print("\t. data = ", data_bool, ", type =",type(data_bool), ",\n")
