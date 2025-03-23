package serializzazioneJSON;

import originali.Autore;
import originali.Libreria;
import originali.Libro;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Vector;

public class LibreriaJSON extends Libreria {
    public LibreriaJSON(){super();}

    public boolean SalvaSuFile(String nomefile) throws IOException {
        boolean stato=false;
        FileWriter fw = new FileWriter(nomefile);
        fw.write("{\n");
        fw.write("\t\"Costo pagina fisso\": "+Libro.getCostoPagina()+",\n");
        fw.write("\t\"Libri\":[" + "\n");
        int k = 0;
        for(Libro l:getLibri()){
            fw.write("\t\t{ \n");
            fw.write("\t\t\"Autore\": {\n"
                    +"\t\t\t\"cognome\": \""+l.getAutore().getCognome()+ "\",\n"
                    +"\t\t\t\"nome\": \""+l.getAutore().getNome()+ "\"\n \t\t\t}, \n"
                    + "\t\t\"Titolo\": \""+ l.getTitolo()+"\",\n"
                    + "\t\t\"Numero pagine\": " + l.getNumeroPagine() + "\n");
            if(k<getLibri().size()-1){
                fw.write("\t\t},\n");
            }else{
                fw.write("\t\t}\n");
            }
            k++;
        }
        fw.write("\t]\n");
        fw.write("}");
        fw.close();
        return stato;
    }


    public void caricaDaFile(String nomeFile) throws IOException {

    }
}
