package com.dicoding.fire.adapter

import android.annotation.SuppressLint
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.RecyclerView
import com.dicoding.fire.R
import com.dicoding.fire.fragment.FragmentDetailKebakaran
import com.dicoding.fire.model.ModelKebakaranBerpotensi
import java.text.ParseException
import java.text.SimpleDateFormat

class AdapterBerpotensi(private val modelKebabkaranBerpotensi: List<ModelKebakaranBerpotensi>): RecyclerView.Adapter<AdapterBerpotensi.ViewHolder>() {
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.list_kebakaran_berpotensi, parent, false)
        return ViewHolder(view)
    }

    @SuppressLint("SimpleDateFormat")
    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        val data = modelKebabkaranBerpotensi[position]
        var lastUpdate = data.strTanggal
        val formatDefault = SimpleDateFormat("dd-MMM-yy")
        val formatTime = SimpleDateFormat("EEE, dd MMM yyyy")

        try {
            val timesFormatLast = formatDefault.parse(lastUpdate)
            lastUpdate = formatTime.format(timesFormatLast)
        } catch (e: ParseException) {
            e.printStackTrace()
        }

        val skalaPotensi = data.strMagnitude//data.strMagnitude?
        val strPotensiTsunami: String
        strPotensiTsunami = if (skalaPotensi!! > 7.0.toString()){
            "Berpotensi Tsunami"
        } else{
            "Tidak berpotensi tsunami"
        }

        holder.tvTanggal.text = lastUpdate + " " + data.strWaktu
        holder.tvWilayah.text = data.strWilayah
        holder.tvKedalaman.text = "Kedalaman : " + data.strKedalaman
        holder.tvSkala.text = data.strMagnitude

        if (skalaPotensi > 0.toString()) {
            holder.tvPotensi.text = strPotensiTsunami
        } else {
            holder.tvPotensi.text = strPotensiTsunami
        }

        holder.tvSkala.setOnClickListener { view ->
            val fragment: Fragment = FragmentDetailKebakaran()
            val bundle = Bundle()
            bundle.putString("StrLintang", data.strLintang)
            bundle.putString("StrBujur", data.strBujur)
            bundle.putString("StrTanggal", data.strTanggal)
            bundle.putString("StrMagnitude", data.strMagnitude)
            bundle.putString("StrKedalaman", data.strKedalaman)
            bundle.putString("StrWilayah", data.strWilayah)
            fragment.arguments = bundle
            val fragmentManager = (view.context as AppCompatActivity).supportFragmentManager
            val fragmentTransaction = fragmentManager.beginTransaction()
            fragmentTransaction.replace(R.id.fragmentContainer, fragment)
            fragmentTransaction.commit()
        }
    }

    override fun getItemCount(): Int {
        return modelKebabkaranBerpotensi.size
    }

    class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        var tvTanggal: TextView
        var tvKedalaman: TextView
        var tvSkala: TextView
        var tvWilayah: TextView
        var tvPotensi: TextView

        init {
            tvTanggal = itemView.tvTanggal
            tvKedalaman = itemView.tvKedalaman
            tvSkala = itemView.tvSkala
            tvWilayah = itemView.tvWilayah
            tvPotensi = itemView.tvPotensi
        }
    }
}