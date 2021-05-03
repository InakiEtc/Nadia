package com.example.demo;

public class Residencia {
    private String provincia;
    private int transitorias;
    private int temporarias;
    private int permanentes;
    private int total;

    public Residencia(String provincia,int transitorias, int temporarias, int permanentes, int total) {
        this.provincia = provincia;
        this.transitorias = transitorias;
        this.temporarias = temporarias;
        this.permanentes = permanentes;
        this.total = total;
    }

    public String getProvincia() {
        return provincia;
    }
    public int getTransitorias() {
        return transitorias;
    }
    public int getTemporarias() {
        return temporarias;
    }
    public int getPermanentes() {
        return permanentes;
    }
    public int getTotal() {
        return total;
    }

    public void setProvincia(String provincia) {
        this.provincia = provincia;
    }
    public void setTransitorias(int transitorias) {
        this.transitorias = transitorias;
    }
    public void setTemporarias(int temporarias) {
        this.temporarias = temporarias;
    }
    public void setPermanentes(int permanentes) {
        this.permanentes = permanentes;
    }
    public void setTotal(int total) {
        this.total = total;
    }
}
