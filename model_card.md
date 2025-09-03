# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

This is a Random Forest Classifier model with default hyperparameters from the SKLearn library.

## Intended Use

This model can be used to predict salary above $50k per year based on census data.

## Training Data

The training datset came from the US census in 1994. 80% of the data was used to train the model.

## Evaluation Data

The evaluation (test) dataset contained the remaining 20% of the data.

## Metrics

The metrics that were evaluated were, Precision: 0.7419 | Recall: 0.6384 | F1: 0.6863.

## Ethical Considerations

There could be a concern of using race, sex, or age to discriminate outcomes by weighing these features too heavily.

## Caveats and Recommendations

Very basic cleaning was performed on the data. More feature engineering could increase the metrics for a better outcome.
