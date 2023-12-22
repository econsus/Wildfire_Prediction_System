package com.dicoding.fire.activity

import android.Manifest
import android.content.pm.PackageManager
import android.location.Criteria
import android.location.LocationListener
import android.location.LocationManager
import android.os.Build
import android.os.Bundle
import android.text.format.DateFormat
import androidx.annotation.RequiresApi
import androidx.appcompat.app.AppCompatActivity
import androidx.coordinatorlayout.widget.CoordinatorLayout
import androidx.core.app.ActivityCompat
import androidx.fragment.app.Fragment
import androidx.fragment.app.FragmentManager
import com.dicoding.fire.R
import com.dicoding.fire.fragment.FragmentBerpotensi
import com.dicoding.fire.fragment.FragmentTerkini
import com.dicoding.fire.networking.ApiEndpoint
import com.dicoding.fire.utils.BottomBarBehavior
import nl.joery.animatedbottombar.AnimatedBottomBar
import java.util.Calendar

@Suppress("DEPRECATION")
class MainActivity : AppCompatActivity(), LocationListener {
    
    var fragmentManager: FragmentManager? = null
    var strTanggal: String? = null
    var permissionArrays = arrayOf(Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_COARSE_LOCATION)
    var latitude = 0.0
    var longtitude = 0.0

    @RequiresApi(Build.VERSION_CODES.M)
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        //permission
        val VersionAndroid = Build.VERSION.SDK_INT
        if (VersionAndroid > Build.VERSION_CODES.LOLLIPOP_MR1) {
            if (checkIfAlreadyhavePermission() && checkIfAlreadyhavePermission2()) {
            } else {
                requestPermissions(permissionArrays, 101)
            }
        }

        //hide show tab
        val layoutParams = tabNavigation.getLayoutParams() as CoordinatorLayout.LayoutParams
        layoutParams.behavior = BottomBarBehavior()
        if (savedInstanceState == null) {
            tabNavigation.selectTabById(R.id.tabDirasakan, true)
            fragmentManager = supportFragmentManager
            val fragmentDirasakan = FragmentDirasakan()
            fragmentManager!!.beginTransaction().replace(R.id.frameContainer, fragmentDirasakan).commit()
        }

        //fragment
        tabNavigation.setOnTabSelectListener(object : AnimatedBottomBar.OnTabSelectListener {
            override fun onTabSelected(lastIndex: Int, lastTab: AnimatedBottomBar.Tab?, newIndex: Int, newTab: AnimatedBottomBar.Tab) {
                var fragment: Fragment? = null
                when (newTab.id) {
                    R.id.tabDirasakan -> fragment = FragmentDirasakan()
                    R.id.tabBerpotensi -> fragment = FragmentBerpotensi()
                    R.id.tabSkala -> fragment = FragmentTerkini()
                }
                if (fragment != null) {
                    fragmentManager = supportFragmentManager
                    fragmentManager!!.beginTransaction().replace(R.id.frameContainer, fragment).commit()
                }
            }
        })
        
        getToday()
        getLatLong()
        
    }
    
    private fun getLatLong() {
        if (ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED && 
            ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(this, arrayOf(Manifest.permission.ACCESS_FINE_LOCATION), 115)
            return
        }
        
        val locationManager = getSystemService(LOCATION_SERVICE) as LocationManager
        val criteria = Criteria()
        val provider = locationManager.getBestProvider(criteria, true)
        val location = locationManager.getLastKnownLocation(provider)
        if (location != null) {
            onLocationChanged(location)
        } else{
            locationManager.requestLocationUpdates(provider, 20000,0f, this)
        }
    }
    private fun getToday() {
        val date = Calendar.getInstance().time
        val defaultDate = DateFormat.format("d MMM yyyy", date) as String
        val formatToday = "$strTanggal, $defaultDate"
        tvDate.text = formatToday
    }

    private fun getCuacaToday() {
        AndroidNetworking.get(ApiEndpoint.URL_CUACA)
            .addPathParameter("lat", latitude.toString())
            .addPathParameter("lon", longitude.toString())
            .addPathParameter("API key", "YOUR API KEY OpenWeather")
            .setPriority(Priority.MEDIUM)
            .build()
            .getAsJSONObject(object : JSONObjectRequestListener {
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
}