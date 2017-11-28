package org.tensorflow.demo;

import android.app.Activity;
import android.content.Intent;
import android.os.Handler;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

public class SplashActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_splash);

        Handler handle = new Handler();
        handle.postDelayed(new Runnable() {
            @Override
            public void run() {
                showClassifier();
            }
        }, 2000);

    }

    private void showClassifier() {
        Intent intent = new Intent(SplashActivity.this,
                ClassifierActivity.class);
        startActivity(intent);
        finish();
    }
}
