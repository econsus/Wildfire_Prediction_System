package com.dicoding.fire.adapter

import android.annotation.SuppressLint
import android.view.LayoutInflater
import android.view.View
import android.widget.TextView
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.dicoding.fire.R
import com.dicoding.fire.adapter.AdapterBerpotensi.ViewHolder
import com.dicoding.fire.model.ModelKebakaranTerjadi
import java.text.ParseException
import java.text.SimpleDateFormat

class AdapterTerjadi(private val modelKebakaranTerjadi:
                     List<ModelKebakaranTerjadi>) : RecyclerView.Adapter<AdapterTerjadi.ViewHolder>() {
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.list_kebakaran_terjadi, parent, false)
        return ViewHolder(view)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        val data = modelKebakaranTerjadi[position]
        var lastUpdate = data.strTanggal
        val formatDefault = SimpleDateFormat("dd/MM/yyyy-HH:mm:ss")
        val formatTime = SimpleDateFormat("EEE, dd MMM yyyy / HH:mm:ss")

        try {
            val timesFormatLast = formatDefault.parse(lastUpdate)
            lastUpdate = formatTime.format(timesFormatLast)
        } catch (e: ParseException) {
            e.printStackTrace()
        }

        holder.tvTanggal.text = lastUpdate
        holder.tvTerjadi.text = "Dirasakan : " + data.strDirasakan
        holder.tvKedalaman.text = "Kedalaman : " + data.strKedalaman
        holder.tvSkala.text = data.strMagnitude + "\nSR"
        holder.tvKeterangan.text = data.strKeterangan
        holder.tvPosisi.text = data.strKoordinat
    }

    override fun getItemCount(): Int {
        return modelKebakaranTerjadi.size
    }

    class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        var tvTanggal: TextView
        var tvTerjadi: TextView
        var tvKedalaman: TextView
        var tvSkala: TextView
        var tvKeterangan: TextView
        var tvPosisi: TextView

        init {
            tvTanggal = itemView.tvTanggal
            tvTerjadi = itemView.tvDirasakan
            tvKedalaman = itemView.tvKedalaman
            tvSkala = itemView.tvSkala
            tvPosisi = itemView.tvPosisi
            tvKeterangan = itemView.tvKeterangan
        }


    }


}