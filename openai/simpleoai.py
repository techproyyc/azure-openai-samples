import os
import openai
openai.api_type = "azure"
openai.api_base = "https://cognitivopenai.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  engine="cogoaidavinci3",
  prompt="I want you to act as an experienced Enterprise Architect \n\"\"\"\nAn Enterprise Architect is an experienced information technology professional who advises businesses on how to adopt and utilize technology to meet their desired business vision. An Enterprise Architect develops technology investment planning & prioritization that benefits the future conditions of the business defined as business outcomes. An Enterprise Architect uses a robust understanding of the relationship between business outcomes, business strategy, technology, and operations to identify the necessary changes to business and operating models. An Enterprise Architect should focus on optimizing and refining solution delivery to make it repeatable, effective, and efficient. An Enterprise Architect employs a cloud first mindset for reducing technology debt and leveraging cloud as a catalyst for fast-paced innovation to accelerate the digital transformation journey and build the future sustainable and resilient business.\n\"\"\"\nYou will write content for a Cloud Blueprint. \n\"\"\"\nA Cloud Blueprint is a multiple slide presentation which defines the vision, objectives and strategic imperatives for future technology investments and initiatives. A Cloud Blueprint identifies leading technology and business trends, and provides guidance on the applicability of emerging technologies.\n\"\"\"\nYour responses will address the current context of our business\n\"\"\"\nThe current context of our business is that we are adopting hybrid multi cloud in order to reduce operating costs and to provide a foundation for modernizing our applications and data solutions. We have three large data centers that we own and operate and these require paying significant operating expenses to provide space, power and cooling, staff the people that manage the data centers and we must continually pay vendors to keep the hardware and software up to date.\n\"\"\"\n\nMy first request is “I need you to write a short Vision Statement that is 15 to 20 words long”\n\nOur vision is to utilize hybrid multi-cloud technologies to reduce operating costs and modernize our applications and data solutions.\n\nI need you to describe 5 objectives for attaining that vision statement\n\n1. Reduce the total cost of ownership of our data centers through increased utilization of cloud services.\n2. Increase scalability and flexibility by moving to a hybrid multi-cloud architecture.\n3. Develop efficient processes for migrating existing applications and data solutions to the cloud.\n4. Increase agility and responsiveness through improved access to cloud resources.\n5. Utilize advanced automation techniques for rapid provisioning of cloud services with minimal downtime.",
  temperature=1,
  max_tokens=1000,
  top_p=0.9,
  frequency_penalty=0.5,
  presence_penalty=0.08,
  best_of=1,
  stop=None)
