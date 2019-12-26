lines = [];
bandera = 1;
muestra = '';
colors = [];
with open("banner.txt",'r') as raw_file:
    lines = raw_file.readlines();
    raw_file.seek(0);
    muestra = raw_file.readline()[0];
    raw_file.seek(0);
    colors = raw_file.readline().split(" ")[1].strip("\n").split(".");
lines.pop(0);
for line in lines:
    for letra in line:
        if(letra == ' '):
            if(bandera != 1):
                bandera = 1;
                with open("banner_new.txt",'+a') as output:
                    output.write("\\e[0m");
        elif(letra == muestra):
            if(bandera != 2):
                bandera = 2;
                with open("banner_new.txt",'+a') as output:
                    output.write("\\e["+colors[0]+"m");
        else:
            if(bandera != 0):
                bandera = 0;
                with open("banner_new.txt",'+a') as output:
                    output.write("\\e["+colors[1]+"m");
        with open("banner_new.txt",'+a') as output:
            output.write(letra);
