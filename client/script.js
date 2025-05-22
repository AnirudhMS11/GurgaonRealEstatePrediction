window.onload = async function () {
  const propSelect = document.getElementById("property");
  const locSelect = document.getElementById("location");
 
  // Hardcoded fallback options
  const defaultProps = ["RESIDENTIAL APARTMENT"];
  const defaultLocs = ["other"];
 
  // Fetch property types
  try {
const propRes = await fetch("http://127.0.0.1:5000/get-property-type");
    const propData = await propRes.json();
    const propTypes = [...defaultProps, ...propData.property_type];
 
    propTypes.forEach(type => {
      const opt = document.createElement("option");
      opt.value = type;
      opt.text = type;
      propSelect.add(opt);
    });
  } catch (err) {
    alert("Error loading property types");
  }
 
  // Fetch locations
  try {
const locRes = await fetch("http://127.0.0.1:5000/get-location");
    const locData = await locRes.json();
    const locations = [...defaultLocs, ...locData.locations];
 
    locations.forEach(loc => {
      const opt = document.createElement("option");
      opt.value = loc;
      opt.text = loc;
      locSelect.add(opt);
    });
  } catch (err) {
    alert("Error loading locations");
  }
 
  // Form submit handler
  document.getElementById("predict-form").addEventListener("submit", async function (e) {
    e.preventDefault();
 
    const area = document.getElementById("area").value;
    const bhk = document.getElementById("bhk").value;
    const propType = document.getElementById("property").value;
    const location = document.getElementById("location").value;
 
    const formData = new FormData();
    formData.append("AREA", area);
    formData.append("BEDROOM_NUM", bhk);
    formData.append("PROPERTY_TYPE", propType);
    formData.append("location", location);
 
    try {
const res = await fetch("http://127.0.0.1:5000/get-price", {
        method: "POST",
        body: formData
      });
      const data = await res.json();
      document.getElementById("result").innerText = `Estimated Price: ₹ ${data.estimated_price} Lakhs`;
    } catch (err) {
      document.getElementById("result").innerText = "Error getting prediction";
    }
  });
}