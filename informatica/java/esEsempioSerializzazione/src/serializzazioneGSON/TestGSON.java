package serializzazioneGSON;

import originali.Autore;
import originali.Libreria;
import originali.Libro;

import java.io.File;
import java.io.IOException;

import java.io.IOException;

public class TestGSON {
    public static void main(String[] args) throws IOException {
        //nome del file in cui andare a salvare nella directory del progetto
        String nomeFile = "libreria.json";
        //est sarà = .bin per chi utilizza il file di byte
        //         = .json
        //         = .csv

        Autore collodi = new Autore("Carlo", "Collodi");
        Autore perrault = new Autore("Charles", "Perrault");

        Libro l1 = new Libro("Pinocchio", collodi, 150);
        Libro l2 = new Libro("Pollicino", perrault, 80);
        Libro l3 = new Libro("La bella addormentata nel bosco", perrault, 50);

        //instanziare un tipo di libreria appropriato
        Libreria libreria = new Libreria();
        // inserimento volumi
        libreria.addVolume(l1);
        libreria.addVolume(l2);
        libreria.addVolume(l3);
        //cambio il prezzo a pagina
        Libro.setCostoPagina(0.01);
        System.out.println(libreria);

        // SERIALIZZAZIONE salvataggio libreria su file METODO DA IMPLEMENTARE
        //LibreriaCsv.salvaSuFile(nomeFile);
        // creazione nuova libreria vuota
        LibreriaGSON l = new LibreriaGSON();
        l.addVolume(l1);
        l.addVolume(l2);
        l.addVolume(l3);
        l.salvaSuFileGSON(nomeFile);
        System.out.println("Prima " + l);
        // DESERIALIZZAZIONE caricamento libreria da file METODO DA IMPLEMENTARE
        //l.caricaDaFile(nomeFile);
        System.out.println("Dopo: " + l);

    }
}

