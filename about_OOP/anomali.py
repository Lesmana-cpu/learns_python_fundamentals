class anomali:
    
    jumlah = 0
    
    def __init__(self,name,jenis,kekuatan,watak):
        self.__name = name
        self.__jenis = jenis
        self.__skill = kekuatan
        self.__penokohan = watak
        if self.__penokohan.lower() == "baik":
            sifat = True
        elif self.__penokohan.lower() == "jahat":
            sifat = False
        else:
            sifat = None

        self.__sifat = sifat
        
        anomali.jumlah += 1
        
    @property
    def info(self):
        pass
    
    @info.getter
    def info(self):
        return f"Name = {self.__name}\njenis = {self.__jenis}\nskill = {self.__skill}\nsifat = {self.__sifat}"
    
    
anml_1 = anomali("suki","pokemon","sangat cerdas","baik")
anml_2 = anomali("ambaroes","Human","air putih penyembuh","Liar")
anml_3 = anomali("cimut","orc","kedipan imiut","Jahat")



print(anml_1.info)
print("\n")
print(anml_2.info)
print("\n")
print(anml_3.info)
