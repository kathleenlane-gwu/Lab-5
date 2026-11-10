library(dplyr)
library(stringr)
library(lubridate)
library(tidyr)

samples <- read.csv("data/messy_samples.csv", stringsAsFactors = FALSE)
samples[13, 'sex']
samples[samples == ""] <- NA
samples2 <- samples %>%
  mutate(
    clean_sample_id = str_remove(
      str_replace(sample_id, "^s", "S"),
      "\\-"
    ),
    
    clean_dob = dob %>%
      str_replace_all("\\.", "/") %>%
      parse_date_time(orders = c("mdy", "ymd", "dby")) %>%
      as.Date(),
    
    clean_sex = sex %>%
      str_replace("Female|f", "F") %>%
      str_replace("m|Male", "M") %>%
      str_replace("unknown", "U") %>%
      replace_na("U"),
    
    clean_enrollment_site = str_replace(str_replace(str_replace(str_replace(str_replace(
      enrollment_site, "ITE-", "ite "), "s", "S"), "eB", "e B"), "_a", " A"), "  ", " "
    )) %>%
  
  filter(
    str_to_lower(glucose_unit) != "mmol/l",
    !is.na(glucose_value),
    glucose_value != "N/A"
  ) %>%
  
  mutate(
    clean_glucose_value = str_remove(
      glucose_value, "\\*"
    ),
    
    clean_glucose_unit = str_replace(
      glucose_unit, "MG/DL|mg/dl", "mg/dL"
    ),
    
    clean_patient_name = str_replace(str_replace(
      patient_name, "KIM", "Kim"), "DAVIS", "Davis"
    )
    
  )

samples2 <- samples2 %>%
  select(
    sample_id = clean_sample_id,
    glucose_value = clean_glucose_value,
    glucose_unit = clean_glucose_unit,
    patient_name = clean_patient_name,
    dob = clean_dob,
    sex = clean_sex,
    enrollment_site = clean_enrollment_site,
    notes
  )

head(samples2)

write.csv(samples2, "results/clean_samples.csv", row.names = FALSE, na = "")