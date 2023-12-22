package com.dicoding.fire.views

interface MainPresenter {
    fun getDataKebakaranTerjadi()
    fun getDataKebakaranBerpotensi()
    fun onProses(proses: Boolean)
}