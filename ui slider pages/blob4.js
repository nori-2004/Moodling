document.addEventListener("DOMContentLoaded", function () {
    const slider = document.getElementById("slider");
    const blobImage = document.getElementById("blobImage");
    const nextButton = document.querySelector(".next-button");

    let lastImage = ""; // Store the last image to detect transitions

    // Function to map slider values to image filenames
    function getImage(value) {
        if (value <= 0.7) {
            return "cmd-f.png";  // Happy blob
        } else if (value <= 1.5) {
            return "cmd-f2.png"; // Neutral blob
        } else if (value <= 2.5) {
            return "cmd-f3.png";
        } else if (value <= 3.7) {
            return "cmd-f4.png"; // Sad blob
        } else {
            return "caffeine.png";
        }
    }

    // Function to update the image and trigger animation only on transition
    function updateBlobImage() {
        let value = parseInt(slider.value);
        let newImage = getImage(value);

        if (newImage !== lastImage) { // Only animate if image changes
            blobImage.src = newImage;
            lastImage = newImage; // Update last image state

            // Remove animation, force reflow, then re-add it
            blobImage.classList.remove("bob-animation");
            void blobImage.offsetWidth; // Forces reflow
            blobImage.classList.add("bob-animation");
        }
    }

    // Attach event listener to update image and animate only on transition
    slider.addEventListener("input", updateBlobImage);

    // Initialize the correct image on page load
    updateBlobImage();

    // Function to update the slider track color dynamically
    function updateSliderTrack() {
        let value = ((slider.value - slider.min) / (slider.max - slider.min)) * 100;
        slider.style.background = `linear-gradient(to right, #02B271 ${value}%, #ccc ${value}%)`;
    }

    // Attach event listener to update slider track
    slider.addEventListener("input", updateSliderTrack);

    // Initialize the slider track color on page load
    updateSliderTrack();

    nextButton.addEventListener("click", function () {
        localStorage.setItem("caffeineIntake", slider.value);
        createItem();

    });

    const createItem = async () => {
        const newItem = {
            age: parseInt(localStorage.getItem('age')),
            caffeine_intake: parseFloat(localStorage.getItem('caffeineIntake')),
            exercise_time: parseFloat(localStorage.getItem('exerciseHours')),
            sleep_time: parseFloat(localStorage.getItem('sleepHours')),
            screen_time: parseFloat(localStorage.getItem('screenTime')),
        };

        console.log("Sending data:", newItem);

        try {
            const response = await fetch('http://127.0.0.1:8000/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(newItem)
            });


            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || `HTTP error! status: ${response.status}`);
            }

            const data = await response.json();

            localStorage.setItem("Result", JSON.stringify(data));

            console.log('Success:', data);
            
            window.location.href = "../ui result page/results copy.html";
        } catch (error) {
            console.error('Error:', error);
        }

    };

});
