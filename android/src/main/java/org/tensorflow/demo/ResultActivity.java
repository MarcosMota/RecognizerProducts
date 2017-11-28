package org.tensorflow.demo;

import android.app.Activity;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;

import java.util.ArrayList;
import java.util.List;

public class ResultActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_result);
        final List<Classifier.Recognition> results = (ArrayList<Classifier.Recognition>) getIntent().getSerializableExtra("results");
        ListView listaDeCursos = (ListView) findViewById(R.id.lista);

        ArrayAdapter<Classifier.Recognition> adapter = new ArrayAdapter<Classifier.Recognition>(this,
                android.R.layout.simple_list_item_1, results);

        listaDeCursos.setAdapter(adapter);

    }
}
