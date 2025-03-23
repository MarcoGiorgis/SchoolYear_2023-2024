package serializzazioneGSON;

import com.google.gson.Gson;
import originali.Libreria;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class LibreriaGSON extends Libreria {
    public LibreriaGSON(){super();}

    public void CaricaDaFile(String nomeFile) throws FileNotFoundException {
        Gson gson = new Gson();
        FileReader fr = new FileReader(nomeFile);
        LibreriaGSON lib = gson.fromJson(fr, LibreriaGSON.class);
        this.setLibri(lib.getLibri());
    }
    public void salvaSuFileGSON(String nomeFile) throws IOException{
        Gson gson = new Gson();
        String json = gson.toJson(this);
        System.out.println("Stringa json\n" + json);

        FileWriter fw = new FileWriter(nomeFile);
        fw.write(json);
        fw.flush();
        fw.close();
    }
}
