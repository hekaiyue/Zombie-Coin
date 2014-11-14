package com.example.zcoins;

import android.os.Bundle;
import android.os.SystemClock;
import android.app.Activity;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Chronometer;
import android.widget.TextView;
import android.support.v4.app.NavUtils;

public class Mine extends Activity {
	private Chronometer timer;
	private static int coins=0;
	private int timesince=0;
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_mine);
		// Show the Up button in the action bar.
		setupActionBar();
		timer =(Chronometer)findViewById(R.id.chronometer1);
		timer.setBase(SystemClock.elapsedRealtime());
		timer.start();
		TextView myTextView = (TextView) findViewById(R.id.coin_count); 
		myTextView.setText("Z-Coins:" + coins);
		TextView myTextView1 = (TextView) findViewById(R.id.lastcoin); 
		myTextView1.setText("Coin found "+timesince+"s ago.");
		Intent i=new Intent(this, Mineservice.class);
		i.putExtra("coins", coins);
		startService(i);
	}

	/**
	 * Set up the {@link android.app.ActionBar}.
	 */
	private void setupActionBar() {

		getActionBar().setDisplayHomeAsUpEnabled(true);

	}
	
	@Override
	protected void onResume()
    {
    	super.onResume();
    	coinBroadcast c=new coinBroadcast();
		TextView myTextView = (TextView) findViewById(R.id.coin_count); 
		myTextView.setText("Z-Coins:" + coins);
    }
	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.mine, menu);
		return true;
	}

	@Override
	public boolean onOptionsItemSelected(MenuItem item) {
		switch (item.getItemId()) {
		case android.R.id.home:
			// This ID represents the Home or Up button. In the case of this
			// activity, the Up button is shown. Use NavUtils to allow users
			// to navigate up one level in the application structure. For
			// more details, see the Navigation pattern on Android Design:
			//
			// http://developer.android.com/design/patterns/navigation.html#up-vs-back
			//
			NavUtils.navigateUpFromSameTask(this);
			return true;
		}
		return super.onOptionsItemSelected(item);
	}
	public static void addCoins(int i)
	{
		coins+=i;
	}

}
