<template>

  <v-container>
    <v-layout
      text-xs-center
      wrap
    >
      <v-flex>
        <!-- IMPORTANT PART! -->
  <v-card width="500" class="mx-auto mt-5">
    <v-card-title>
     <!-- <v-list-item-subtitle>by Bewave</v-list-item-subtitle>    -->
     <v-list-item-avatar color="teal lighten-2"> <h5></h5> </v-list-item-avatar> 
        <h1 class="display-1">Rental Price Prediction</h1>
     <!-- <v-list-item-subtitle>by Bewave</v-list-item-subtitle> -->   
      <v-img
        src="../assets/montreal-skyline.1476282.jpg"
        height="194" >
     </v-img> 
    </v-card-title>  
      <v-card-text>
        <v-form
          ref="form"
          v-model="valid"
          lazy-validation
        >
        <v-container>
          <v-select 
            :items="Neighbor"
            v-model="Neighborhood"
            :rules="[v => !!v || 'Neighborhood is required']"
            label="Neighborhood"
            dense
            required
          ></v-select>
          <v-row>
            <v-col>    
            <v-select 
              :items="property"
              v-model="PropertyType"
              :rules="[v => !!v || 'Property type is required']"
              label="Property type"
              dense
              required
            ></v-select> 
            </v-col>
            <v-col>
            <v-select
              :items="Room"
              v-model="RoomType"
              :rules="[v => !!v || 'Room type is required']"
              label="Room type"
              dense
              required
            ></v-select> 
            </v-col>
          </v-row> 
          <v-row>
            <v-col> 
            <v-text-field
              v-model="NumberRooms"
              :rules="[v => !!v || 'Number of rooms is required']"
              label="Number of rooms"
              required
            ></v-text-field>
            </v-col>
            <v-col>
            <v-text-field
              v-model="NumberBeds"
              :rules="[v => !!v || 'Number of beds is required']"
              label="Number of beds"
              required
            ></v-text-field>
            </v-col>
          </v-row>    
          <v-row>
            <v-col>    
                <v-switch v-model="BedType" label="Real bed ?"></v-switch>
            </v-col>
            <v-col>  
            <v-select
              :items="Travel"
              v-model="Travelers"
              :rules="[v => !!v || 'Number of travelers is required']"
              label="Travelers"
              dense
              required
            ></v-select>
            </v-col>
          </v-row>
          <v-text-field
            v-model="Available"
            :rules="[v => !!v || 'Number of available days is required']"
            label="Number of available days"
            suffix="days"
            required
          ></v-text-field>
          <v-row>
            <v-col>
              <v-switch v-model="InstantBookable" label="Instant bookable ?"></v-switch>
            </v-col>
            <v-col>
              <v-switch v-model="HostSuperhost" label="Are you superhost ?"></v-switch>
            </v-col>
          </v-row>  
          <v-row>
            <v-col>
            <v-text-field
              v-model="NumberReviews"
              :rules="[v => !!v || 'Number of reviews rating is required']"
              label="Number of reviews"
              required
            ></v-text-field>   
            </v-col>
            <v-col>
            <v-text-field
              v-model="ReviewScoresRating"
              :rules="[v => !!v || 'Review scores rating is required']"
              label="Review scores rating"
              suffix="%"
              required
            ></v-text-field>
            </v-col>
          </v-row>  
          </v-container>
        </v-form>
        <v-card-actions>
            <v-btn color="success" dark @click="submit">Predict
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn color="error" dark @click="reset"> Reset
            </v-btn>
        </v-card-actions> 
        </v-card-text>
      </v-card>
        <br/>
        <br/>
      <v-card width="500" class="mx-auto mt-0">        
        <h1  class="text-md-center" v-if="predictedClass">Predicted Price by night : {{ predictedClass }} $</h1>
      </v-card>
<!-- END: IMPORTANT PART! -->
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
  import axios from 'axios'
export default {
    name: 'HelloWorld',
    data: () => ({
      valid: true,
      Neighborhood:null,
      Neighbor: [
        { text: 'Le Plateau-Mont-Royal', value:'26' },
        { text: 'Montréal-Ouest', value:'14' },
        { text: 'Outremont', value:'27' },
        { text: 'Anjou', value:'2' },
        { text: 'Rivière-des-Prairies-Pointe-aux-Trembles', value:'3' },
        { text: 'Sainte-Anne-de-Bellevue', value:'4' },
        { text: 'Villeray-Saint-Michel-Parc-Extension', value:'5' },
        { text: 'Saint-Léonard', value:'6' },
        { text: 'Westmount', value:'30' },
        { text: 'LaSalle', value:'8' },
        { text: 'Mercier-Hochelaga-Maisonneuve', value:'9' },
        { text: 'Pierrefonds-Roxboro', value:'10' },
        { text: 'Verdun', value:'11' },
        { text: 'Côte-des-Neiges-Notre-Dame-de-Grâce', value:'12' },
        { text: 'Hampstead', value:'13' },
        { text: 'Montréal-Nord', value:'1' },
        { text: 'Lachine', value:'15' },
        { text: 'Rosemont-La Petite-Patrie', value:'16' },
        { text: 'Dollard-des-Ormeaux', value:'17' },
        { text: 'Pointe-Claire', value:'18' },
        { text: 'Dorval', value:'19' },
        { text: 'Beaconsfield', value:'20' },
        { text: 'Mont-Royal', value:'22' },
        { text: 'Côte-Saint-Luc', value:'23' },
        { text: 'Kirkland', value:'24' },
        { text: 'Le Sud-Ouest', value:'25' },
        { text: 'Ahuntsic-Cartierville', value:'7' },
        { text: 'Baie-d Urfé', value:'28'},
        { text: 'Baie-d Urfé', value:'29'},
        { text: 'Saint-Laurent', value:'21' },
        { text: 'L Île-Bizard-Sainte-Geneviève', value:'31' },
      ],
      PropertyType:null,
      property: [
        { text: 'Apartment', value:'0' },
        { text: 'Condominium', value:'1' },
        { text: 'House', value:'2' },
        { text: 'Townhouse', value:'4' },
        { text: 'Serviced apartment', value:'5' },
        { text: 'Loft', value:'6' },
        { text: 'Other', value:'3' },
      ],
      RoomType:null,
      Room: [
        { text: 'Entire home/apt', value:'2' },
        { text: 'Private room', value:'1' },
        { text: 'Shared room', value:'0' },
        { text: 'Hotel room', value:'3' },
      ],
      Travelers:null,
      Travel: [
        { text: '1 Traveler', value:'1' },
        { text: '2 Travelers', value:'2' },
        { text: '3 Travelers', value:'3' },
        { text: '4 Travelers', value:'4' },
        { text: '5 Travelers', value:'5' },
        { text: '6 Travelers', value:'6' },
        { text: '7 Travelers', value:'7' },
        { text: '8 Travelers', value:'8' },
        { text: '9 Travelers', value:'9' },
        { text: '10 Travelers', value:'10' },
        { text: '11 Travelers', value:'11' },
        { text: '12 Travelers', value:'12' },
        { text: '13 Travelers', value:'13' },
        { text: '14 Travelers', value:'14' },
        { text: '15 Travelers', value:'15' },
        { text: '16 Travelers', value:'16' },
        { text: '17 Travelers', value:'17' },
        { text: '18 Travelers', value:'18' },
      ],
      BedType:'',
      NumberRooms: '',
      NumberBeds: '',
      Available: '',
      NumberReviews: '',
      ReviewScoresRating: '',
      predictedClass : '',
      InstantBookable: '',
      HostSuperhost: '',
    }),
    methods: {
    submit () {
      this.$refs.form.validate()
      // http://ai-rentals-api.bewave.io:8060/predict
      axios.post('http://ai-rentals-api.bewave.io:8060/predict', {
        neighborhood_: this.Neighborhood,
        propertytype_: this.PropertyType,
        roomtype_: this.RoomType,
        travelers_: this.Travelers,
        number_rooms: this.NumberRooms,
        number_beds: this.NumberBeds,
        bed_type: this.BedType ? '1' : '0',
        available_: this.Available,
        instant_bookable: this.InstantBookable ? '1' : '0',
        host_superhost: this.HostSuperhost ? '1' : '0',
        number_reviews: this.NumberReviews,
        review_scores_rating: this.ReviewScoresRating,
      })
      .then((response) => {
        this.predictedClass = response.data.class
      })
    },
      reset () {
      this.$refs.form.reset()
    },
  },
}
</script>