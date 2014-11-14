package com.example.zcoins;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.content.SharedPreferences.Editor;
import android.os.Bundle;
import android.telephony.TelephonyManager;
import android.view.Menu;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends Activity 
{
	public static SharedPreferences settings;
	public static Editor editor;
	public static String id = "";
	
    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        settings = getSharedPreferences("zcoin", 0);
        editor = settings.edit();
        editor.clear();
        editor.commit();
        if(settings.contains("userid")){
        	id = settings.getString("userid", "");
        	setContentView(R.layout.activity_main);
        }else{
        	setContentView(R.layout.splash);
        }
    }
   
    @Override
    public boolean onCreateOptionsMenu(Menu menu) 
    {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }
    
    public void mineZCoins(View view)
    {
    	Intent intent = new Intent(this, Mine.class);
    	startActivity(intent);
    }
    
    public void friendsView(View view)
    {
    	Intent intent = new Intent(this, FriendsList.class);
    	startActivity(intent);
    }
    
    public void loadmainscreen(View view){
    	TelephonyManager tMgr = (TelephonyManager)this.getSystemService(Context.TELEPHONY_SERVICE);
    	String mPhoneNumber = tMgr.getLine1Number();
    	char[] cs = mPhoneNumber.toCharArray();
    	String s = "";
    	for (char c:cs){
    		if(Character.isDigit(c)){
    			s += c;
    		}
    	}
    	HTTPHandler.login(s);
    	editor.putString("userid", s);
    	editor.apply();
    	id = s;
    	setContentView(R.layout.activity_main);
    }
    public void Andrew(View view)
    {
    	EditText idtxt = (EditText) findViewById(R.id.andrew);
    	String id = idtxt.getText().toString();
    	String name= HTTPHandler.andrewLogin(id);
    	idtxt.setText("Hi"+name);
    	if(name!=null)
    	{
    	Button andrewButton = (Button) findViewById(R.id.andrew_button);
    	andrewButton.setText("Hi"+name);
    	}
    }
}
